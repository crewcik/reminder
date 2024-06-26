import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import schedule
import time

def show_notification(title, message):
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo(title, message)

def schedule_task(hour, minute, task):
    def task_function():
        show_notification("Bildirim", task)
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(task_function)

def schedule_exit():
    show_notification("Program Çıkışı", "Program otomatik olarak sonlandırıldı.")
    time.sleep(5) 
    exit()

def add_task():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    task = task_entry.get()
    schedule_task(hour, minute, task)
    hour_entry.delete(0, tk.END)
    minute_entry.delete(0, tk.END)
    task_entry.delete(0, tk.END)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = tk.Tk()
root.title("Crew - Hatırlatıcı Ekle")
root.resizable(False, False)  

center_window(root)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)

hour_label = ttk.Label(frame, text="Saat:")
hour_label.grid(row=0, column=0, sticky="e")
hour_entry = ttk.Entry(frame, width=5)
hour_entry.grid(row=0, column=1)

minute_label = ttk.Label(frame, text="Dakika:")
minute_label.grid(row=1, column=0, sticky="e")
minute_entry = ttk.Entry(frame, width=5)
minute_entry.grid(row=1, column=1)

task_label = ttk.Label(frame, text="Görev:")
task_label.grid(row=2, column=0, sticky="e")
task_entry = ttk.Entry(frame, width=20)
task_entry.grid(row=2, column=1)

add_button = ttk.Button(frame, text="Görev Ekle", command=add_task)
add_button.grid(row=3, columnspan=2)

root.mainloop()

schedule.every().day.at("06:30").do(schedule_exit)

while True:
    schedule.run_pending()
    time.sleep(1)
