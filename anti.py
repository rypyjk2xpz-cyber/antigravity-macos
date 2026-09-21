#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
from pathlib import Path

OLD_BYTES = b"ineligible"
NEW_BYTES = b"inexigible"

SEARCH_PATHS = [
    Path("/Applications"),
    Path.home() / "Applications",
    Path.home() / "Library/Application Support",
    Path.home() / ".antigravity",
]

TARGET_NAMES = {
    "language_server",
    "language_server_macos_arm",
    "language_server_macos_arm64",
    "language_server_macos_x64",
    "agy",
}

def find_targets():
    found = set()
    print("🔍 Поиск файлов Antigravity на Mac...")
    for base in SEARCH_PATHS:
        if not base.exists():
            continue
        try:
            for root, _, files in os.walk(base):
                for f in files:
                    if f in TARGET_NAMES:
                        p = Path(root) / f
                        if os.access(p, os.X_OK) and not p.is_symlink():
                            found.add(p.resolve())
        except PermissionError:
            continue
    return sorted(list(found))

def patch_file(file_path: Path):
    print(f"\nОбработка: {file_path}")
    
    with open(file_path, "rb") as f:
        data = f.read()

    if NEW_BYTES in data and OLD_BYTES not in data:
        print("  ✓ Уже пропатчен ранее.")
        return False

    if OLD_BYTES not in data:
        print("  - Метка 'ineligible' не найдена (пропуск).")
        return False

    backup_path = file_path.with_suffix(file_path.suffix + ".bak")
    if not backup_path.exists():
        shutil.copy2(file_path, backup_path)
        print(f"  ✓ Создан бэкап: {backup_path.name}")

    occurrences = data.count(OLD_BYTES)
    patched_data = data.replace(OLD_BYTES, NEW_BYTES)

    with open(file_path, "wb") as f:
        f.write(patched_data)
    print(f"  ✓ Заменено вхождений: {occurrences}")

    print("  ✓ Обновление цифровой подписи бинарника...")
    subprocess.run(["codesign", "--force", "--deep", "-s", "-", str(file_path)], check=True)
    return True

def fix_app_bundle():
    app_path = Path("/Applications/Antigravity.app")
    if app_path.exists():
        print("\n🍏 Обновление подписи бандла Antigravity.app...")
        subprocess.run(["codesign", "--force", "--deep", "-s", "-", str(app_path)], check=False)
        subprocess.run(["xattr", "-cr", str(app_path)], check=False)
        print("  ✓ Подпись приложения обновлена, карантин снят.")

def main():
    targets = find_targets()
    if not targets:
        print("❌ Файлы Antigravity не найдены.")
        sys.exit(1)

    print(f"Найдено файлов для проверки: {len(targets)}")
    patched = 0
    for target in targets:
        if patch_file(target):
            patched += 1

    fix_app_bundle()

    print(f"\n🎉 Готово! Пропатчено: {patched}")
    print("👉 Включите зарубежный VPN и запускайте Antigravity.")

if __name__ == "__main__":
    main()
