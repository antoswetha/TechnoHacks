import tkinter as tk

def on_click(event):
    # Get the text of the button clicked
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Evaluate the expression and display the result
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        # Clear the entry field
        entry.delete(0, tk.END)
    else:
        # Append the clicked button's text to the entry field
        entry.insert(tk.END, text)

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry field to display the input and output
entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(ipadx=10, ipady=10, padx=10, pady=10)

# Create the buttons for the calculator
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for text in row:
        button = tk.Button(frame, text=text, font=("Helvetica", 20), relief=tk.GROOVE, width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

# Run the main event loop
root.mainloop()
