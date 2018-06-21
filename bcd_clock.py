from microbit import *

# initial values
hours = 12
minutes = 0
seconds = 0


def split_to_digits(n):
    """
    Splits a decimal number to two digits and returns it as a tuple.
    N.B.: this function does not check whether the input is a
    two-digit decimal number.
    """
    return n // 10, n % 10


def to_binary(n):
    """
    Convert a decimal number to a four digit binary number
    represented by a four element array.
    For example input is 7, then the output is [0, 1, 1, 1].
    N.B.: this function does not check whether the input fits
    to the four-digit representation, so it is at most sixteen.
    """
    b4 = n // 8
    l1 = n % 8
    b3 = l1 // 4
    l2 = l1 % 4
    b2 = l2 // 2
    l3 = l2 % 2
    b1 = l3 % 2
    return [b4, b3, b2, b1]


def draw():
    """
    Sets the LEDs to draw the BCD digits.

    It uses the four four-element array representing the binary number
    and sets the LED brightness. It can be specified from 0 to 9, where
    0 means off the 9 is the brightest.
    Hour value is written to the column 0 and 1,
    minute value is written to the column 3 and 4.
    The least significant bits are written to the row 4 and the most
    significant bits to the row 1. Row 0 is unused, so as the column 2.
    """
    h_tens, h_ones = split_to_digits(hours)
    m_tens, m_ones = split_to_digits(minutes)
    for i in range(4):
        if to_binary(h_tens)[i] == 1:
            display.set_pixel(0, i + 1, 8)
        else:
            display.set_pixel(0, i + 1, 0)
        if to_binary(h_ones)[i] == 1:
            display.set_pixel(1, i + 1, 8)
        else:
            display.set_pixel(1, i + 1, 0)
        if to_binary(m_tens)[i] == 1:
            display.set_pixel(3, i + 1, 8)
        else:
            display.set_pixel(3, i + 1, 0)
        if to_binary(m_ones)[i] == 1:
            display.set_pixel(4, i + 1, 8)
        else:
            display.set_pixel(4, i + 1, 0)


while True:
    # this is an endless loop where all the computation happens

    draw()
    # stepper button handling
    if button_a.was_pressed():
        hours += 1
    if button_b.was_pressed():
        minutes += 1

    # increasing time variables
    # N.B.: the cycle is 100 ms so "seconds" counting tenfold faster
    # therefore it has to count to 600 instead of 60.
    if seconds == 600:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0

    # increase second at every cycle
    seconds += 1
    # pause the cycle for 100 ms
    sleep(100)
