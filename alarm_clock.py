import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_hour = int(alarm_time[:2])
        alarm_minute = int(alarm_time[3:5])
        alarm_second = int(alarm_time[6:8])
        alarm_period = alarm_time[9:]
        if alarm_period.upper() not in ['AM', 'PM']:
            raise ValueError
        if alarm_hour > 12 or alarm_minute > 59 or alarm_second > 59:
            raise ValueError
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        current_hour = int(current_time[:2])
        current_minute = int(current_time[3:5])
        current_second = int(current_time[6:8])
        current_period = current_time[9:]
        if alarm_period.upper() == 'AM' and current_period == 'PM':
            alarm_hour += 12
        elif alarm_period.upper() == 'PM' and current_period == 'AM':
            alarm_hour += 12
        elif alarm_hour == 12 and current_hour != 12:
            alarm_hour = 0
        elif alarm_hour != 12 and current_hour == 12:
            current_hour = 0
        time_diff = datetime.timedelta(
            hours=alarm_hour-current_hour,
            minutes=alarm_minute-current_minute,
            seconds=alarm_second-current_second
        )
        time.sleep(time_diff.total_seconds())
        messagebox.showinfo("Alarm", "Wake up!")
        winsound.PlaySound("E:\codeclause\Alarm_clock_withGUI\sound.wav", winsound.SND_FILENAME)
    except ValueError:
        messagebox.showerror("Error", "Invalid alarm time format!")

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (HH:MM:SS AM/PM):", font=("Arial", 14))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Set Alarm", font=("Arial", 14), command=set_alarm)
button.pack(pady=20)

root.mainloop()
