import pyautogui
from tkinter import *


def create_window():
    win = Tk()
    # Dimensions
    # Make the window borderless
    win.overrideredirect(True)
    # Always on top
    win.wm_attributes("-topmost",True)
    # Set window transparency (requires a window manager that supports it)
    # win.attributes('-alpha', 0.5)
    # Configure border style and color
    win.configure(highlightbackground="red", highlightcolor="red", highlightthickness=1)
    return win

def main():
    print("Exit with Ctr+C\n\n")
    try:
        win = create_window()
        label = Label(win, text= "", font=('Time New Roman', 10), fg="red")
        while True:
            p = pyautogui.position() # Get mouse pos
            print(str(p) + "                                                 ", end='\r') # print
            labeltext = f'{p.x},{p.y}' # new label text
            win.geometry(str(len(labeltext) * 8) + "x20") # adjust window size
            label.config(text=labeltext) # update label text
            label.pack()
            win.geometry(f'+{p.x+10}+{(p.y + 30) if (p.y - 30 <= 0) else p.y-30}') # move window, automatically flips on top edge of the screen
            win.update()
    except KeyboardInterrupt:
        win.destroy()
        print('\nExit...\n')

if __name__ == "__main__":
    main()
