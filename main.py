import sys
from tkinter import *
from turtle import *
import logging
from canvasutils import *
from tkinter import colorchooser

root = Tk()
bg_color = "#ffffff"


def main(window):
    global bg_color
    debug = "--debug" in sys.argv

    logging.basicConfig(level=logging.DEBUG if debug else logging.WARN)
    bg_color = "#454545" if debug else "#2e2e2e"


    tkinter_version = Tcl().eval("info patchlevel")
    logging.debug(f"Using {tkinter_version}")

    canvas, turtle, button = initialize_ui(window=window)



    root.mainloop()


def initialize_ui(window):
    canvas = Canvas(
        window,
        height=500,
        width=750,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.grid(padx=10, pady=10)

    actuator_btn = Button(
        window,
        text="Start",
        width="15",
        height="2",
        background="#454545",
        activebackground="#2b2b2b",
        foreground="#ffffff",
        activeforeground="#ffffff",
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    actuator_btn.grid(padx=20, pady=20)

    window.title("Guess The Note")
    window.configure(background="#2e2e2e")

    turtle = RawTurtle(canvas=canvas)

    turtle.speed(0)
    turtle.hideturtle()

    draw_bg(turtle, bg_color)

    return canvas, turtle, actuator_btn




if __name__ == '__main__':
    main(window=root)
