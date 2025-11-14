import tkinter as tk
from tkinter import messagebox, END

first = 0
op = None

# ======== FUNCTIONS ========
def update_display(value):
    """Show value in the display (replace previous)."""
    display.config(state='normal')
    display.delete('1.0', END)
    display.insert(END, value)
    display.config(state='disabled')

def press_num(num):
    display.config(state='normal')
    display.insert(END, num)
    display.config(state='disabled')

def press_op(operator):
    global first, op
    try:
        first = float(display.get('1.0', END).strip())
        op = operator
        update_display("")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def calculate():
    global first, op
    try:
        second = float(display.get('1.0', END).strip())
        if op == '+':
            result = first + second
        elif op == '-':
            result = first - second
        elif op == '*':
            result = first * second
        elif op == '/':
            if second == 0:
                messagebox.showerror("Error", "Math Error (Divide by Zero)")
                update_display("")
                return
            result = first / second
        elif op == '%':
            result = first % second
        else:
            messagebox.showerror("Error", "Invalid Operation")
            return
        update_display(str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

def clear():
    update_display("")

# ======== GUI SETUP ========
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="#1e1e1e")
root.geometry("320x480")

# ======== DISPLAY (MULTILINE) ========
display = tk.Text(root, font=('Segoe UI', 28, 'bold'), bg="#2d2d2d", fg="white",
                  height=2, wrap='word', borderwidth=0, relief='flat')
display.pack(fill='x', padx=10, pady=20, ipady=10)
display.insert(END, "")
display.config(state='disabled')  # user can't type manually

# ======== FRAME FOR BUTTONS ========
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill='both')

# ======== BUTTON STYLING ========
button_style = {
    "font": ('Segoe UI', 18, 'bold'),
    "bd": 0,
    "relief": 'flat',
    "highlightthickness": 0,
    "activebackground": "#3a3a3a",
    "activeforeground": "white",
}

def create_btn(text, row, col, color="#2d2d2d", cmd=None):
    btn = tk.Button(frame, text=text, bg=color, fg="white", command=cmd, **button_style)
    btn.grid(row=row, column=col, sticky='nsew', padx=4, pady=4, ipadx=5, ipady=5)

# ======== BUTTON GRID ========
buttons = [
    ('7', 1, 0, '#2d2d2d'), ('8', 1, 1, '#2d2d2d'), ('9', 1, 2, '#2d2d2d'), ('/', 1, 3, '#ff9500'),
    ('4', 2, 0, '#2d2d2d'), ('5', 2, 1, '#2d2d2d'), ('6', 2, 2, '#2d2d2d'), ('*', 2, 3, '#ff9500'),
    ('1', 3, 0, '#2d2d2d'), ('2', 3, 1, '#2d2d2d'), ('3', 3, 2, '#2d2d2d'), ('-', 3, 3, '#ff9500'),
    ('0', 4, 0, '#2d2d2d'), ('.', 4, 1, '#2d2d2d'), ('%', 4, 2, '#2d2d2d'), ('+', 4, 3, '#ff9500'),
]

for (text, r, c, color) in buttons:
    if text in ['+', '-', '*', '/', '%']:
        action = lambda t=text: press_op(t)
    else:
        action = lambda t=text: press_num(t)
    create_btn(text, r, c, color, action)

# Clear & Equal
create_btn('C', 5, 0, '#d32f2f', clear)
create_btn('=', 5, 1, '#43a047', calculate)
tk.Label(frame, text='', bg="#1e1e1e").grid(row=5, column=2, columnspan=2)

# ======== GRID CONFIG ========
for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

root.mainloop()