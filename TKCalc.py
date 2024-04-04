import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += symbol
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = result
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)
    except:
        clear_field()
        text_result.insert(tk.END, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete("1.0", tk.END)

root = tk.Tk()
root.geometry("260x400")
text_result = tk.Text(root, height = 2, width = 16 , font = ("Arial", 24))
text_result.grid(row = 0, column = 0, columnspan = 5)

symbols = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "C", "0", "=", "/", "(", ")"]
btns = []

for i,symbol in enumerate(symbols):
    if symbol == "=":
        btns.append(tk.Button(root, text = symbol, font = ("Arial", 24), command = evaluate_calculation))
    elif symbol == "C":
        btns.append(tk.Button(root, text = symbol, font = ("Arial", 24), command = clear_field))
    else:
        btns.append(tk.Button(root, text = symbol, font = ("Arial", 24), command = lambda s = symbol: add_to_calculation(s)))
    btns[i].grid(row = i // 4 + 1, column = i % 4)
root.mainloop()
