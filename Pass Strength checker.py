import tkinter as tk
import re

def check_pass():
    
    password = password_ent.get()

    length_criteria = len(password) >= 8
    digit_criteria = bool(re.search(r"\d", password))
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    symbol_criteria = bool(re.search(r"[!@#$%^&*().,?:{}|<>]", password))
    
    criteria_met = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, symbol_criteria])
    
    if criteria_met <= 2:
        strength = "Weak"
    elif criteria_met == 3 or criteria_met == 4:
        strength = "Medium"
    else:
        strength = "Strong"
        
    result_l.config(text= f"Password Strength: {strength}")
    
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

password_l = tk.Label(root, text = "Enter Password: ")
password_l.pack(pady = 10)

password_ent = tk.Entry(root, show = "*")
password_ent.pack(pady = 5)

check_btn = tk.Button(root, text = "Check Strength", command = check_pass)
check_btn.pack(pady = 10)

result_l = tk.Label(root, text = "")
result_l.pack(pady = 10)

root.mainloop()