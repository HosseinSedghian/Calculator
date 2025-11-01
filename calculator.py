import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg="#1B1818")

# Operands and operators
op1 = 0.0
op2 = 0.0
operator = ""
operatorFlag = False

# Configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

# Create buttons
def btn1_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "1")
btn1 = tk.Button(root, text="1", bg="#444444", fg="white", command=btn1_command)

def btn2_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "2")
btn2 = tk.Button(root, text="2", bg="#444444", fg="white", command=btn2_command)

def btn3_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "3")
btn3 = tk.Button(root, text="3", bg="#444444", fg="white", command=btn3_command)

def btn4_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "4")
btn4 = tk.Button(root, text="4", bg="#444444", fg="white", command=btn4_command)

def btn5_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "5")
btn5 = tk.Button(root, text="5", bg="#444444", fg="white", command=btn5_command)

def btn6_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "6")
btn6 = tk.Button(root, text="6", bg="#444444", fg="white", command=btn6_command)

def btn7_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "7")
btn7 = tk.Button(root, text="7", bg="#444444", fg="white", command=btn7_command)

def btn8_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "8")
btn8 = tk.Button(root, text="8", bg="#444444", fg="white", command=btn8_command)

def btn9_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "9")
btn9 = tk.Button(root, text="9", bg="#444444", fg="white", command=btn9_command)

def btnneg_command():
    if eres.get().startswith("-"):
        eres.delete(0, 1)
    else:
        eres.insert(0, "-")
btnneg = tk.Button(root, text="+/-", bg="#444444", fg="white", command=btnneg_command)

def btn0_command():
    if eres.get() == "0":
        eres.delete(0, tk.END)
    eres.insert(tk.END, "0")
btn0 = tk.Button(root, text="0", bg="#444444", fg="white", command=btn0_command)

def btndot_command():
    eres.insert(tk.END, ".")
btndot = tk.Button(root, text=".", bg="#444444", fg="white", command=btndot_command)

def btnpercent_command():
    global op2
    op2 = float(eres.get())
    if operator == "*":
        op2 = op2 / 100.0
    if operator == "+" or operator == "-":
        op2 = op1 * (op2 / 100.0)
    eres.delete(0, tk.END)
    eres.insert(tk.END, op2)
btnpercent = tk.Button(root, text="%", bg="#313131", fg="white", command=btnpercent_command)

def btnCE_command():
    eres.delete(0, tk.END)
    eres.insert(tk.END, "0")
    global operatorFlag
    operatorFlag = False
btnCE = tk.Button(root, text="CE", bg="#313131", fg="white", command=btnCE_command)

def btnC_command():
    eres.delete(0, tk.END)
    eres.insert(tk.END, "0")
    etemp.delete(0, tk.END)
    global operatorFlag
    operatorFlag = False
btnC = tk.Button(root, text="C", bg="#313131", fg="white", command=btnC_command)

def btnremove_command():
    if eres.get() == "0":
        return
    else:
        eres.delete(len(eres.get()) - 1, tk.END)
        if len(eres.get()) == 0:
            eres.insert(tk.END, "0")
btnremove = tk.Button(root, text="⌫", bg="#313131", fg="white", command=btnremove_command)

def makeup_operations(inputX : str):
    etemp.insert(0, f"{eres.get()} {inputX} ")
    global op1
    op1 = float(eres.get())
    global operator
    operator = inputX
    eres.delete(0, tk.END)
    eres.insert(tk.END, "0")

def unary_operation(inputOpp : str):
    etemp.insert(0, f"{inputOpp}{eres.get()}")
    global op1
    op1 = float(eres.get())
    if op1.is_integer():
        op1 = int(op1)
    eres.delete(0, tk.END)
    if inputOpp == "√":
        result = math.sqrt(op1)
        if result.is_integer():
            result = int(result)
        eres.insert(0, str(result))
    if inputOpp == "^":
        result = math.pow(op1, 2)
        if result.is_integer():
            result = int(result)
        eres.insert(0, str(result))
    if inputOpp == "1/":
        result = 1.0 / op1
        if result.is_integer():
            result = int(result)
        eres.insert(0, str(result))

def btnrev_command():
    unary_operation("1/")
btnrev = tk.Button(root, text="1/x", bg="#313131", fg="white", command=btnrev_command)

def btnpow2_command():
    unary_operation("^")
btnpow2 = tk.Button(root, text="x²", bg="#313131", fg="white", command=btnpow2_command)

def btnsqrt_command():
    unary_operation("√")
btnsqrt = tk.Button(root, text="√x", bg="#313131", fg="white", command=btnsqrt_command)

def btndiv_command():
    global operatorFlag
    if operatorFlag == False:
        operatorFlag = True
        makeup_operations("/")
    else:
        double_operations("/")
btndiv = tk.Button(root, text="÷", bg="#313131", fg="white", command=btndiv_command)

def btnmul_command():
    global operatorFlag
    if operatorFlag == False:
        operatorFlag = True
        makeup_operations("*")
    else:
        double_operations("*")
btnmul = tk.Button(root, text="×", bg="#313131", fg="white", command=btnmul_command)

def btnsubt_command():
    global operatorFlag
    if operatorFlag == False:
        operatorFlag = True
        makeup_operations("-")
    else:
        double_operations("-")
btnsubt = tk.Button(root, text="-", bg="#313131", fg="white", command=btnsubt_command)

def btnsum_command():
    global operatorFlag
    if operatorFlag == False:
        operatorFlag = True
        makeup_operations("+")
    else:
        double_operations("+")
btnsum = tk.Button(root, text="+", bg="#313131", fg="white", command=btnsum_command)

def double_operations(inputOperator):
    global op2
    op2 = float(eres.get())
    if op2.is_integer():
        op2 = int(op2)
    global operator
    global op1
    tempstring = etemp.get()
    etemp.delete(0, tk.END)
    etemp.insert(tk.END, f"{tempstring} {op2} {inputOperator}")
    if operator == "+":
        result = op1 + op2
        op1 = result
        operator = inputOperator
    elif operator == "-":
        result = op1 - op2
        op1 = result
        operator = inputOperator
    elif operator == "*":
        result = op1 * op2
        op1 = result
        operator = inputOperator
    elif operator == "/":
        result = op1 / op2
        op1 = result
        operator = inputOperator
    eres.delete(0, tk.END)
    eres.insert(tk.END, "0")

def result_makeup(inputResult):
    global op1
    global op2
    if op1.is_integer():
        op1 = int(op1)
    if op2.is_integer():
        op2 = int(op2)
    if inputResult.is_integer():
        inputResult = int(inputResult)
    inputResult = round(inputResult, 2)
    eres.delete(0, tk.END)
    eres.insert(tk.END, str(inputResult))
    etemp.delete(0, tk.END)
    etemp.insert(tk.END, f"{op1} {operator} {op2} = ")
    
def btnequal_command():
    global op2
    op2 = float(eres.get())
    global operatorFlag
    operatorFlag = False
    if operator == "+":
        result = op1 + op2
        result_makeup(result)
    if operator == "-":
        result = op1 - op2
        result_makeup(result)
    if operator == "*":
        result = op1 * op2
        result_makeup(result)
    if operator == "/":
        result = op1 / op2
        result_makeup(result)
btnequal = tk.Button(root, text="=", bg="#2C9CC9", fg="white", command=btnequal_command)

# Create Entries
# Keyboard bindings.
def on_key_press(event):
    key = event.char
    if key in "0123456789":
        if eres.get() == "0":
            eres.delete(0, tk.END)
        eres.insert(tk.END, key)
        return "break"
    elif key == "+":
        btnsum_command()
        return "break"
    elif key == "-":
        btnsubt_command()
        return "break"
    elif key == "*":
        btnmul_command()
        return "break"
    elif key == "/":
        btndiv_command()
        return "break"
    elif key == ".":
        btndot_command()
        return "break"
    elif key == "\r":
        btnequal_command()
        return "break"
    elif key.lower() == "c":
        btnC_command()
        return "break"
    elif event.keysym == "BackSpace":
        btnremove_command()
        return "break"
    # elif event.keysym == "Delete":
    #     btnCE_command()
    #     btnC_command()
    #     return "break"
root.bind("<Key>", on_key_press)

eres = tk.Entry(root, validate="key")
etemp = tk.Entry(root)

# Place entries in the grid
etemp.grid(row=0, column=0, columnspan=4, sticky="nsew")
etemp.configure(bg="#313131", fg="#AFAAAA", font=("Segoe UI", 16), justify="right")

eres.grid(row=1, column=0, columnspan=4, sticky="nsew")
eres.configure(bg="#313131", fg="white", font=("Segoe UI", 20), justify="right")
eres.insert(tk.END, "0")

# Place buttons in the grid
btnneg.grid(row=7, column=0, sticky="nsew", padx=1, pady=1)
btn0.grid(row=7, column=1, sticky="nsew", padx=1, pady=1)
btndot.grid(row=7, column=2, sticky="nsew", padx=1, pady=1)
btnequal.grid(row=7, column=3, sticky="nsew", padx=1, pady=1)

btn1.grid(row=6, column=0, sticky="nsew", padx=1, pady=1)
btn2.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)
btn3.grid(row=6, column=2, sticky="nsew", padx=1, pady=1)
btnsum.grid(row=6, column=3, sticky="nsew", padx=1, pady=1)

btn4.grid(row=5, column=0, sticky="nsew", padx=1, pady=1)
btn5.grid(row=5, column=1, sticky="nsew", padx=1, pady=1)
btn6.grid(row=5, column=2, sticky="nsew", padx=1, pady=1)
btnsubt.grid(row=5, column=3, sticky="nsew", padx=1, pady=1)

btn7.grid(row=4, column=0, sticky="nsew", padx=1, pady=1)
btn8.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)
btn9.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)
btnmul.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)

btnrev.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)
btnpow2.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
btnsqrt.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)
btndiv.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)

btnpercent.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
btnCE.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
btnC.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
btnremove.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

# Run the application
root.mainloop()
