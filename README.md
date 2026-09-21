# Antigravity Unlocker for macOS 🍏

[English](#english) | [Русский](#русский)

---

## English

A lightweight unlocker script to bypass regional restrictions for Google Antigravity on macOS (Apple Silicon and Intel).

### How It Works
The script locates the `language_server` binary inside `Antigravity.app`, patches the `ineligible` protobuf flag to `inexigible`, re-signs the application bundle via `codesign` to prevent the "App is damaged" error, and clears the quarantine flag.

> ⚠️ **Important:** This patch lifts the account-level restriction. You **must use a system-wide foreign VPN** to route AI model queries.

### Quick Start

1. Quit Antigravity completely (`Cmd + Q`).
2. Run in Terminal:

```bash
# Download the script
curl -O [https://raw.githubusercontent.com/rypyjk2xpz-cyber/antigravity-macos/main/anti.py](https://raw.githubusercontent.com/rypyjk2xpz-cyber/antigravity-macos/main/anti.py)

# Run with sudo
sudo python3 anti.py
```
*(Enter your macOS administrator password when prompted).*

3. Turn on your foreign VPN and launch Antigravity!

---

### Troubleshooting

#### 1. `PermissionError: Operation not permitted`
If macOS blocks file modification even with `sudo`:
* Go to **System Settings** → **Privacy & Security** → **App Management** (or **Full Disk Access**).
* Enable access for **Terminal**.
* Restart Terminal (`Cmd + Q`) and re-run `sudo python3 anti.py`.

#### 2. Error 400 / Cached Bad Session
If you had a failed login attempt before running the patch:
1. Quit Antigravity.
2. Open **Keychain Access**, search for `Antigravity`, and remove all matching credentials.
3. Clear session cache via Terminal:
```bash
rm -rf ~/Library/Application\ Support/Antigravity/Cache* ~/Library/Application\ Support/Antigravity/Cookies* ~/Library/Application\ Support/Antigravity/Session*
```
4. Connect to your VPN and log in again.

### Rollback
```bash
sudo cp /Applications/Antigravity.app/Contents/Resources/bin/language_server.bak /Applications/Antigravity.app/Contents/Resources/bin/language_server
sudo codesign --force --deep -s - /Applications/Antigravity.app
```

---

## Русский

Скрипт для снятия региональной блокировки Google Antigravity на macOS (Apple Silicon M-серии и Intel).

### Как это работает
Скрипт находит бинарник `language_server` внутри `Antigravity.app`, заменяет проверку protobuf-флага `ineligible` на `inexigible`, обновляет цифровую подпись приложения (`codesign`), чтобы система не ругалась на поврежденный файл, и снимает флаг карантина macOS.

> ⚠️ **Важно:** Скрипт разблокирует сам аккаунт. Для отправки запросов к модели вам **обязательно нужен включенный зарубежный системный VPN**.

### Быстрый запуск

1. Полностью закройте Antigravity (`Cmd + Q`).
2. Откройте Терминал и выполните:

```bash
# Скачиваем скрипт
curl -O [https://raw.githubusercontent.com/rypyjk2xpz-cyber/antigravity-macos/main/anti.py](https://raw.githubusercontent.com/rypyjk2xpz-cyber/antigravity-macos/main/anti.py)

# Запускаем от администратора
sudo python3 anti.py
```
*(Терминал попросит пароль от вашего Mac. Символы при вводе отображаться не будут — введите пароль и нажмите Enter).*

3. Включите зарубежный VPN и запускайте Antigravity!

---

### Возможные проблемы и решения

#### 1. Ошибка `PermissionError: Operation not permitted`
Если macOS не дает скрипту изменить файл даже под `sudo`:
* Перейдите в **Системные настройки** → **Конфиденциальность и безопасность** → **Управление приложениями** (App Management) или **Полный доступ к диску** (Full Disk Access).
* Включите тумблер напротив **Терминал** (Terminal).
* Перезапустите Терминал (`Cmd + Q`) и повторите команду `sudo python3 anti.py`.

#### 2. Ошибка 400 (старый кэш после неудачного входа)
Если до использования скрипта вы уже пытались зайти без VPN:
1. Закройте Antigravity.
2. Откройте **Связку ключей** (Keychain Access) через Spotlight, найдите `Antigravity` и удалите найденные записи.
3. Выполните сброс кэша в Терминале:
```bash
rm -rf ~/Library/Application\ Support/Antigravity/Cache* ~/Library/Application\ Support/Antigravity/Cookies* ~/Library/Application\ Support/Antigravity/Session*
```
4. Включите зарубежный VPN и войдите заново.

### Откат изменений
```bash
sudo cp /Applications/Antigravity.app/Contents/Resources/bin/language_server.bak /Applications/Antigravity.app/Contents/Resources/bin/language_server
sudo codesign --force --deep -s - /Applications/Antigravity.app
```

---

### Keywords & Error Search / Для поиска

Этот патч решает следующие проблемы и ошибки:
* `User location is not supported` (Google Antigravity macOS / OS X)
* `Error 400: ineligible account`
* `language_server` patch for Mac (Apple Silicon M1/M2/M3/M4 & Intel)
* Приложение Antigravity повреждено и не может быть открыто (Code Signature Invalid / SIGKILL)
* Как запустить Antigravity в России на Mac
* Antigravity Google bypass region lock macOS
