from tkinter import *
import math

val = ""
A = 0
operator = ""
myPage=""
flag=True
myVal=''

img = PhotoImage(file='1.png')
Label(splash_root,image=img, anchor= CENTER).pack()
#canvas.create_image(400 , 400 ,anchor=CENTER, image=img)
splash_root.title("MY_Calculator")
splash_root.geometry("600x625+550+550")
splash_root.eval('tk::PlaceWindow . center')
splash_root.overrideredirect(True)


def ross():
    splash_root.destroy()
    root = Tk()
    root.title("Calculator")
    root.configure(background='white')
    root.resizable(width=True, height=True)
    root.geometry("520x590+350+50")

    # Click_Functions

    def btn_1_is_clicked():
        global val
        val = val + "1"
        ans.set(val)

    def btn_2_is_clicked():
    exit()    
        global val
        val = val + "2"
        ans.set(val)

    def btn_3_is_clicked():
        global val
        val = val + "3"
        ans.set(val)

    def btn_4_is_clicked():
        global val
        val = val + "4"
        ans.set(val)

    def btn_5_is_clicked():
        global val
        val = val + "5"
        ans.set(val)

    def btn_6_is_clicked():
        global val
        val = val + "6"
        ans.set(val)

    def btn_7_is_clicked():
        global val
        val = val + "7"
        ans.set(val)

    def btn_8_is_clicked():
        global val
        val = val + "8"
        ans.set(val)

    def btn_9_is_clicked():
        global val
        val = val + "9"
        ans.set(val)

    def btn_0_is_clicked():
        global val
        val = val + "0"
        ans.set(val)

    def btn_dot_is_clicked():
        global val
        val = val + "."
        ans.set(val)

    def btn_exp_is_clicked():
        global A
        global operator
        global val
        A = float(val)
        operator = "^"
        val = val + "^"
        ans.set(val)

    def btn_log_is_clicked():
        global A
        global operator
        global val
        A = float(val)
        operator = "log"
        val = "log("+str(A)+")"
        ans.set(val)

    def btn_root_is_clicked():
        global A
        global operator
        global val
        A = float(val)
        operator = "\u221A"
        val = val + "\u221A"
        ans.set(val)


    # Operation_Functions
    def exponential_number():
        exponential = number.get() ** power.get()
        ans.set(exponential)

    def log_number():
        result = math.log(val)
        ans.set(result)

    def root_number():
        rootnumber = number.get() ** (1 / power.get())
        ans.set(rootnumber)

    def dot():
        global val
        result = val+"."
        ans.set(result)

    def equals():
        global A
        global operator
        global val
        val2 = val

        if operator == "^":
            x = float((val2.split("^")[1]))
            result = A ** x
            val=str(result)
            ans.set(result)

        if operator == "log":
            result = math.log10(A)
            val = str(result)
            ans.set(result)

        if operator == "\u221A":
            x = int((val2.split("\u221A")[1]))
            result = (x**(1/A))
            val = str(result)
            ans.set(result)

    def clear():
        global val
        if val=="log":
            # text=val[:-3]
            # val=text
            ans.set("")
        else:
            text=val[:-1]
            val=text
            ans.set(text)
        # val = ""

    def clearAll():
        global val
        val = ""
        ans.set(val)


    number = IntVar()
    power = IntVar()
    ans = StringVar()


    txtDisplay = Entry(root, font=('Bahnschrift Light', 20, 'bold'),
                       bg='black', fg='white',
                       bd=30, width=28, textvariable=ans, justify=RIGHT)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)

    #entry_pad
    btn0 = Button(root, text=0, width=6, height=2,
    bg='black', fg='white', command=btn_0_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=5, column=1, columnspan=1, pady=1)



    btn1 = Button(root, text=1, width=6, height=2,
    bg='black', fg='white', command=btn_1_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=2, column=0, pady=1)



    btn2 = Button(root, text=2, width=6, height=2,
    bg='black', fg='white', command=btn_2_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=2, column=1, pady=1)



    btn3 = Button(root, text=3, width=6, height=2,
    bg='black', fg='white', command=btn_3_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=2, column=2, pady=1)



    btn4 = Button(root, text=4, width=6, height=2,
    bg='black', fg='white', command=btn_4_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=3, column=0, pady=1)



    btn5 = Button(root, text=5, width=6, height=2,
    bg='black', fg='white', command=btn_5_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=3, column=1, pady=1)



    btn6 = Button(root, text=6, width=6, height=2,
    bg='black', fg='white', command=btn_6_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=3, column=2, pady=1)



    btn7 = Button(root, text=7, width=6, height=2,
    bg='black', fg='white', command=btn_7_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=4, column=0, pady=1)



    btn8 = Button(root, text=8, width=6, height=2,
    bg='black', fg='white', command=btn_8_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=4, column=1, pady=1)



    btn9 = Button(root, text=9, width=6, height=2,
    bg='black', fg='white', command=btn_9_is_clicked,
    font=('Bahnschrift Light', 20, 'bold'),
    bd=4, ).grid(row=4, column=2, pady=1)


    btnRt = Button(root, text="\u221A", width=6, height=2,
    bg='black', fg='white',font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command=btn_root_is_clicked
    ).grid(row=4, column=3, pady=1)



    btnExp = Button(root, text="^", width=6, height=2,
    bg='black', fg='white',font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command=btn_exp_is_clicked
    ).grid(row=2, column=3, pady=1)



    btnLog = Button(root, text="log", width=6, height=2,
    bg='black',fg='white', font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command=btn_log_is_clicked
    ).grid(row=3, column=3, pady=1)



    btnDot = Button(root, text=".", width=6, height=2,
    bg='black', fg='white',font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command= btn_dot_is_clicked
    ).grid(row=5, column=0, pady=1)



    btnClear = Button(root, text=chr(67), width=6, height=2,
    bg='black',fg='white', font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command=clear,
    ).grid(row=5, column=3, columnspan=1, pady=1)



    btnAllClear = Button(root, text=chr(67) + chr(69), width=30, height=2,
    bg='black',fg='white', font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command=clearAll,
    ).grid(row=6, columnspan=4, pady=1)



    btnEquals = Button(root, text="=", width=6, height=2,
    bg='black',fg='white', font=('Bahnschrift Light', 20, 'bold'),
    bd=4, command=equals,
    ).grid(row=5, column=2, pady=1)




    root.mainloop()

mainloop()
