import tkinter as tk

import time


def update_clock():

    current_time = time.strftime('%H:%M:%S')  # Get the current time in HH:MM:SS format

    label.config(text=current_time)  # Update the label with the current time

    label.after(1000, update_clock)  # Call this function again after 1000 milliseconds (1 second)


# Create the main window

root = tk.Tk()

root.title('Simple Clock')


# Create a label to display the time

label = tk.Label(root, font=('Helvetica', 48), fg='black')

label.pack()


update_clock()  # Start the clock

root.mainloop()  # Run the application