# import tkinter as tk

# # Function to update the expression in the text entry box
# def click(event):
#     text = event.widget.cget("text")
#     if text == "=":
#         try:
#             result = str(eval(str(entry.get())))
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, result)
#         except:
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, "Error")
#     elif text == "C":
#         entry.delete(0, tk.END)
#     else:
#         entry.insert(tk.END, text)

# # Create main window
# root = tk.Tk()
# root.title("Simple Calculator")
# root.geometry("300x400")

# # Entry field to show the input and result
# entry = tk.Entry(root, font="Arial 20")
# entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# # Button layout
# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["C", "0", "=", "+"]
# ]

# # Create buttons dynamically
# for row in buttons:
#     frame = tk.Frame(root)
#     for btn in row:
#         button = tk.Button(frame, text=btn, font="Arial 18", width=4, height=2)
#         button.pack(side=tk.LEFT, padx=5, pady=5)
#         button.bind("<Button-1>", click)
#     frame.pack()

# # Start the application
# root.mainloop()


# For Drak theme

import tkinter as tk

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Dark Mode Calculator")
root.geometry("320x450")
root.configure(bg="#121212")  # Dark background

# Entry widget
entry = tk.Entry(root, font="Consolas 22", bg="#1e1e1e", fg="white", bd=5, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, padx=15, pady=20, ipady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Button styles
btn_bg = "#333333"
btn_fg = "#ffffff"
btn_active_bg = "#555555"

for row in buttons:
    frame = tk.Frame(root, bg="#121212")
    for btn_text in row:
        btn = tk.Button(
            frame,
            text=btn_text,
            font="Consolas 18",
            bg=btn_bg,
            fg=btn_fg,
            activebackground=btn_active_bg,
            width=5,
            height=2,
            relief=tk.FLAT
        )
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)
    frame.pack(pady=5)

# Start the app
root.mainloop()
