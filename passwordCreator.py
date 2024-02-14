try:
    import string
    import random
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox

    LETTERS = string.ascii_letters

    NUMBERS = string.digits

    punctuation = string.punctuation


    # パスワード作成のメインコード
    def password_generator(length=8, moji=False, suji=False, kigo=False):
        password = None
        if moji and suji and kigo:
            password = ''.join([LETTERS, NUMBERS, punctuation])

        elif (moji == True) and (suji == True):

            password = ''.join([LETTERS, NUMBERS])

        elif (moji == True) and (kigo == True):

            password = ''.join([LETTERS, punctuation])

        elif (suji == True) and (kigo == True):

            password = ''.join([NUMBERS, punctuation])

        elif moji:

            password = f'{LETTERS}'

        elif suji:

            password = f'{NUMBERS}'

        elif kigo:

            password = f'{punctuation}'

        else:
            password = f'{LETTERS}{NUMBERS}{punctuation}'

        # ランダムのパスワード作成
        password = list(password)
        random.shuffle(password)

        random_password = random.choices(password, k=length)
        random_password = ''.join(random_password)

        return str(random_password)

    # チェックボックスの状態
    def get_check_box(a):
        if a == 0:
            return False
        elif a == 1:
            return True


    # 桁数の入力　チェック
    def validation(txt):
        if str(txt).isdigit():
            lenth_passWord = int(str(txt))
            if lenth_passWord == 0:
                messagebox.showinfo("注意", '桁数 > 0')
                return 0
            else:
                return int(str(txt))
        else:
            # messagebox
            messagebox.showinfo("注意", '桁数の入力 !!!')
            return 0


    # Display
    window = Tk()
    window.title("RPA")
    # window.geometry("1280x720")

    # Label
    lb = tk.Label(window, text="パスワード作成のアプリ", fg='red', font=("Arial", 30))
    lb.grid(column=1, row=0)

    # Label
    lb_2 = tk.Label(window, text="桁数の入力", fg='green', font=("Arial", 14))
    lb_2.grid(column=1, row=1)

    # Entry ( 入力スペース )
    txt = tk.Entry(window, width=40, font=('Arial', 16))
    txt.grid(column=1, row=2)

    v = tk.StringVar()


    def setText(word):
        v.set(word)


    txt_2 = tk.Entry(window, width=40, font=('Arial', 16), textvariable=v, fg='blue')
    txt_2.grid(column=1, row=9)

    # チェックボックスの状態を確認するvar変数
    var = tk.IntVar()
    c1 = tk.Checkbutton(window, text='文字', variable=var, font=('Arial', 15))
    c1.grid(column=1, row=4)

    var_2 = tk.IntVar()
    c2 = tk.Checkbutton(window, text='数字', variable=var_2, font=('Arial', 15))
    c2.grid(column=1, row=5)

    var_3 = tk.IntVar()
    c3 = tk.Checkbutton(window, text='記号', font=('Arial', 15), variable=var_3)
    c3.grid(column=1, row=6)


    def create():
        global txt

        try:
            moji = get_check_box(var.get())

            suji = get_check_box(var_2.get())

            kigo = get_check_box(var_3.get())

            text = password_generator(int(validation(txt.get())), moji=moji, suji=suji, kigo=kigo)

            setText(text)
        except Exception as ex:
            print(ex)
        return


    # Button
    btn_Create_password = tk.Button(window, text='パスワード作成', command=create, font=('Arial', 14))
    btn_Create_password.grid(column=1, row=7)


    def create_2():
        global txt, lb_2

        moji = get_check_box(var.get())

        suji = get_check_box(var_2.get())

        kigo = get_check_box(var_3.get())

        text = password_generator(random.randint(8, 20), moji=moji, suji=suji, kigo=kigo)

        setText(text)
        return


    # Button
    btn_Create_password_random = tk.Button(window, text='ランダムのパスワードを作成', command=create_2, font=('Arial', 14))
    btn_Create_password_random.grid(column=1, row=8)

    window.mainloop()
except Exception as ex:
    print(ex)
    exit(0)