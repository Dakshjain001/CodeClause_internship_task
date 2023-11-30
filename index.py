import tkinter as tk
from tkinter import ttk
import time
import threading
from playsound import playsound 

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x200")

        self.label = ttk.Label(root, text="Set Alarm (HH:MM:SS)")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root, font=("Helvetica", 24))
        self.entry.pack(pady=10)

        self.button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.button.pack(pady=20)

        self.alarm_thread = None

    def set_alarm(self):
        alarm_time = self.entry.get()
        try:
            alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))
            now = time.localtime()
            current_hour, current_minute, current_second = now.tm_hour, now.tm_min, now.tm_sec

            alarm_seconds = (alarm_hour - current_hour) * 3600 + (alarm_minute - current_minute) * 60 + (
                        alarm_second - current_second)

            if alarm_seconds <= 0:
                raise ValueError("Invalid time. Please set a future time.")

            self.alarm_thread = threading.Thread(target=self.wait_and_play_alarm, args=(alarm_seconds,))
            self.alarm_thread.start()

        except ValueError as e:
            self.label.config(text=str(e), foreground="red")

    def wait_and_play_alarm(self, seconds):
        self.label.config(text=f"Alarm set! Waiting for {seconds} seconds...", foreground="green")
        time.sleep(seconds)
        self.label.config(text="Alarm!", foreground="blue")
        playsound('alarm_sound.mp3')  

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()