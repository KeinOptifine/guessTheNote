from dataclasses import dataclass
from turtle import RawTurtle
from typing import Any
import logging


@dataclass
class State:
    color: tuple[Any, Any] = None
    pos: tuple[float, float] = None


state: State = State()


def save_state(turtle: RawTurtle):
    global state

    if state.color or state.pos:
        logging.warning("A new state was saved while there was still an old one present. it was overwritten")

    logging.debug(f"Original save state: {state}")
    state.color = turtle.color()
    state.pos = turtle.pos()
    logging.debug(f"New save state: {state}")


def restore_state(turtle: RawTurtle):
    global state
    if not state.color or not state.pos:
        logging.warning("function restore_state() in canvasutils.py was called but there was no saved state.")
        return

    turtle.pencolor(state.color[0])
    turtle.fillcolor(state.color[1])
    turtle.goto(state.pos[0], state.pos[1])

    state.color = None
    state.pos = None


def draw_bg(turtle: RawTurtle, color: str):
    save_state(turtle)

    turtle.color(color)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.begin_fill()
    turtle.goto(-750, -500)
    turtle.begin_fill()
    turtle.goto(-750, 500)
    turtle.goto(750, 500)
    turtle.goto(750, -500)
    turtle.end_fill()

    restore_state(turtle)
