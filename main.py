import math
import time
import tkinter as tk
from tkinter import ttk

from ttkbootstrap import Style
from ttkthemes import ThemedTk

root = ThemedTk(theme="yaru")  # Modern theme 'yaru'
root.title("Modern Analog Clock")

# Initialize ttkbootstrap style
style = Style(theme="darkly")  # Modern looking theme

frame = ttk.Frame(root, padding="30 30 30 30")
frame.pack(fill=tk.BOTH, expand=True)

# Create a Canvas to hold the title
title_canvas = tk.Canvas(frame, width=500, height=60, bg='white')
title_canvas.pack(pady=(0, 50))

# Define a font that is modern
modern_font = ('Century Gothic', 20)


# Add the title to your application
title_text = title_canvas.create_text(250, 30, text="The Modern Analog Clock", font=modern_font, fill='white')

# Call the function to start updating the title color

# Adjust the size of canvas
canvas = tk.Canvas(frame, width=500, height=500, bg='white')
canvas.pack(pady=(0, 50))

twelve_hour_format = tk.BooleanVar()
twelve_hour_format.set(True)


def draw_clock():
    canvas.delete('all')
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    am_pm = "AM" if hours < 12 else "PM"

    if twelve_hour_format.get() and hours > 12:
        hours -= 12

    # draw the outer and inner circles
    canvas.create_oval(75, 75, 425, 425, width=0, fill='#bbb')
    canvas.create_oval(85, 85, 415, 415, width=0, fill='#eee')

    # draw the hour numbers
    for i in range(1, 13):
        angle = math.pi / 2 - 2 * math.pi * i / 12
        x = 250 + 100 * math.cos(angle)  # Reduced the radius to 100
        y = 250 - 100 * math.sin(angle)  # Reduced the radius to 100
        canvas.create_text(x, y, text=str(i), font=('Century Gothic', 20), fill='black')

    # draw hour markers
    for i in range(12):
        angle = math.pi / 2 - 2 * math.pi * i / 12
        x1 = 250 + 130 * math.cos(angle)
        y1 = 250 - 130 * math.sin(angle)
        x2 = 250 + 140 * math.cos(angle)
        y2 = 250 - 140 * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=2, fill='black')

    # draw minute markers
    for i in range(60):
        angle = math.pi / 2 - 2 * math.pi * i / 60
        x1 = 250 + 135 * math.cos(angle)
        y1 = 250 - 135 * math.sin(angle)
        x2 = 250 + 140 * math.cos(angle)
        y2 = 250 - 140 * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, fill='black')

    # draw the hands of the clock
    hour_angle = math.pi / 2 - 2 * math.pi * hours / 12
    minute_angle = math.pi / 2 - 2 * math.pi * minutes / 60
    second_angle = math.pi / 2 - 2 * math.pi * seconds / 60

    for name, hand_angle, hand_length, hand_color, hand_width in [
        ("hour", hour_angle, 80, 'gray20', 6),
        ("minute", minute_angle, 120, 'gray30', 4),
        ("second", second_angle, 140, 'red', 2),
    ]:
        end_x = 250 + hand_length * math.cos(hand_angle)
        end_y = 250 - hand_length * math.sin(hand_angle)
        shadow_x = 250 + (hand_length - 2) * math.cos(hand_angle + 0.01)
        shadow_y = 250 - (hand_length - 2) * math.sin(hand_angle + 0.01)
        # Draw shadow for a 3D effect
        canvas.create_line(250, 250, shadow_x, shadow_y, fill='gray50', width=hand_width + 2)
        # Draw the actual hand
        canvas.create_line(250, 250, end_x, end_y, fill=hand_color, width=hand_width)

    # display the time
    if twelve_hour_format.get():
        time_string = time.strftime(f"%I:%M:%S {am_pm}", current_time)
    else:
        time_string = time.strftime("%H:%M:%S", current_time)

    canvas.create_text(250, 470, text=time_string, font=('Century Gothic', 20), fill='white')

    root.after(1000, draw_clock)


draw_clock()

time_format_button = ttk.Button(frame, text='Switch Time Format', style='success.Outline.TButton',
                                command=lambda: twelve_hour_format.set(not twelve_hour_format.get()))
time_format_button.pack(side=tk.LEFT, padx=(0, 20))

developer_label = ttk.Label(frame, font=('Century Gothic', 10),
                            text="Developed by: Abhishek Shah | Developed year: 2023", foreground='white')
developer_label.pack(side=tk.RIGHT, padx=(20, 0))

root.mainloop()
