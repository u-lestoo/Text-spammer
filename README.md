# 🖋️ Python Auto Typing Bot

A simple Python bot that automatically types a chosen string into the active window (e.g., chat, game, browser) and presses **Enter** in a loop until the user types `exit` in the terminal.

---

## 🚀 Features
- Types any text into the currently active window.  
- Automatically presses **Enter** after each message.  
- Repeats messages with a customizable time delay.  
- Runs continuously until you type `exit` to stop it.  
- Works universally — simulates real keyboard input (no API hooks).

---

## 🧰 Requirements

Install the required library:

```bash
pip install pyautogui
```

---

## 📜 Usage

1. Copy the `bot_loop.py` file to your project folder.  
2. Run the program:

   ```bash
   python bot_loop.py
   ```

3. Enter:
   - The text you want the bot to type.  
   - The delay between messages (in seconds).  
4. Click the window where you want the bot to type (you have 5 seconds).  
5. The bot will start typing and pressing **Enter** automatically.  
6. Type `exit` in the terminal to stop the bot.

---

## ⚠️ Warning

This program is **not intended for spam** or for violating the terms of service of any game or application.  
Use it **responsibly** and only for automation or testing on your own computer.

---

## 🧩 Example

```
Enter the text to send: hello
Enter the delay between messages (in seconds): 2

You have 5 seconds to click the window where the bot should type...
Type 'exit' to stop:
```

After starting, the bot will type “hello” every 2 seconds until you type `exit`.

---
