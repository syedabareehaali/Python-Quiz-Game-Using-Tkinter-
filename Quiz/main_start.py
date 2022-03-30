from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Country
            Country.main()
        elif args == 2:
            from Options import Occupation
            Occupation.main()
        elif args == 3:
            from Options import Mobiles
            Mobiles.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Computer
            Computer.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()

    def option():

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#FFEBCD',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="Country",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Occupation",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Mobiles",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Shapes",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Computer",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Quiz ~Fun For Everyone")
    main_window.configure(background="#F0F8FF")
    main_window.iconbitmap(r'quizee_logo_.ico')

    img0 = PhotoImage(file="quizee_logo.png")
    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg='#F0F8FF',
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()
