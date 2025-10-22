import pyautogui
import time
import threading

def pisz_tekst(tekst, delay):
    while not stop_event.is_set():
        pyautogui.typewrite(tekst)
        pyautogui.press("enter")
        time.sleep(delay)
tekst = input("Podaj tekst, który ma być wysyłany: ")
delay = float(input("Podaj odstęp między wysyłaniem (w sekundach): "))

print("\nMasz 5 sekund, żeby kliknąć w okno, w którym bot ma pisać...")
time.sleep(5)
stop_event = threading.Event()
bot_thread = threading.Thread(target=pisz_tekst, args=(tekst, delay))
bot_thread.start()
while True:
    cmd = input("Wpisz 'exit', żeby zatrzymać: ").strip().lower()
    if cmd == "exit":
        stop_event.set()
        bot_thread.join()
        print("✅ Bot zatrzymany.")
        break
