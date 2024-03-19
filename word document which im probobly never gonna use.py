import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Google docs, but cheaper!(and better quality:)")

    Text_edit = tk.Text(window, font="Arial 14")
    Text_edit.grid(row=0, column=0)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="save")
    open_button = tk.Button(frame, text="open")

    save_button.grid(row=0, column=0)
    open_button.grid(row=1,column=0)
    frame.grid(row =0, column=0)

    window.mainloop()

main()
