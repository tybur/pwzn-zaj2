# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
    if not step:
        step = 1
    elif type(step) != type(0):
        raise ValueError("step must be an integer!")

    if not stop:
        stop = start_stop
        start = 0
    else:
        start = start_stop

    if start > stop and step > 0:
        return []
    elif start < stop and step < 0:
        return []

    x = start
    while x < stop:
        yield x
        x += step
