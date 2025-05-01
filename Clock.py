
# Importing necessary libraries
import tkinter as tk
from time import strftime

# Creating the main window
root = tk.Tk()
root.title("Digital Clock")  # Set the title of the window

# Function to update the time
def time():
    # Geting the current time in the desired format
    today = strftime('%H: %M: %S %p \n %D \n %A')
    
    # Updating the label with the current time
    label.config(text=today)
    
    # Calling the time function again after 1000ms (1s) to update the time
    label.after(1000, time)

# Creating a label to display the time
label = tk.Label(root, font=('arial', 40), background="pink", foreground="black")
label.pack(anchor='center')  # Center the label in the window

# Start the time function
time()

# Running the main loop
root.mainloop()


