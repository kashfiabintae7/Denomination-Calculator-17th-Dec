from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg='#6b6f92')
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    Msgbox = messagebox.showinfo("Alert!", "Do you want to calculate denomination count?")
    
    if Msgbox == 'ok':
        topwin()
        
button1 = Button(root, text = "Let's Get Started!", command = msg, bg = '#1e255a', fg = "white")
button1.place(x = 260, y = 360)


def topwin():


    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='#a2a2b9')
    top.geometry("600x350+50+50")

    label=Label(top, text="Enter total amount", bg='#626297')
    entry=Entry(top)
    lbl=Label(top, text="Here are number of notes for each denomination",bg='#8d8dbf')

    l1=Label(top, text='1000',bg='#8c8c9f')
    l2=Label(top, text='500',bg='#a5a5b8')
    l3=Label(top, text='100',bg='#b6b6c3')

    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)
    
    def calculator():
        try:
            global amount
            
            amount = int(entry.get())
            
            note1000 = amount//1000
            amount = amount % 1000
            
            note500 = amount//500
            amount = amount % 500
            
            note100 = amount//100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))            
            t3.insert(END, str(note100))
            
        except ValueError:
            messagebox.showerror("Errror", "Please Enter a Valid Number")
            
    
    
    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50 )
    entry.place(x=200, y=80 )
    btn.place(x=240, y=120 )
    lbl.place(x=140, y=170 )

    l1.place(x=180, y=200 )
    l2.place(x=180, y=230 )
    l3.place(x=180, y=260 )

    t1.place(x=270, y=200 )
    t2.place(x=270, y=230 )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
            
                        
                    
            
            