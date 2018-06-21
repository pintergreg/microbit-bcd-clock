from microbit import *

# initial time value as a binary number
time = 0b0001001000000000
partials = 0


def draw():
    # s = format(time, "016b").replace("1", "8")
    s = "{0:0>16b}".format(time).replace("1", "8")
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html
    # display.show(Image("0%s:0%s:00000:0%s:0%s" % (s[0:4], s[4:8], s[8:12], s[12:16])))
    a = "00000:0%s0%s%s:0%s0%s%s:%s%s0%s%s:%s%s0%s%s" %\
        (s[4], s[8], s[12],
         s[5], s[9], s[13],
         s[2], s[6], s[10], s[14],
         s[3], s[7], s[11], s[15])
    display.show(Image(a))


# draw initial state
draw()

while True:
    # this is an endless loop where all the computation happens

    # normally it is not required to reday the display in an iteration
    needs_to_redraw = False

    # stepper button handling
    if button_a.was_pressed():
        time += 0b0000000100000000
        needs_to_redraw = True
    if button_b.was_pressed():
        time += 0b0000000000000001
        partials = 0
        needs_to_redraw = True

    # As the cycle is 200 ms so "partials" counting five times in a second
    # therefore it has to count to 300 to step a minute.
    if partials == 300:
        time += 0b0000000000000001
        partials = 0
        needs_to_redraw = True

    # increase digits in time variable
    if time & 0b0000000000001111 == 10:
        time = time & 0b1111111111110000
        time += 0b0000000000010000
    if (time & 0b0000000011110000) >> 4 == 6:
        time = time & 0b1111111100001111
        time += 0b0000000100000000
    if (time & 0b0000111100000000) >> 8 == 10:
        time = time & 0b1111000011111111
        time += 0b0001000000000000
    if (time & 0b1111000000000000) >> 12 == 2 and\
       (time & 0b0000111100000000) >> 8 == 4:
        time = time & 0b0000000011111111

    # redraw display if necessary
    if needs_to_redraw:
        draw()

    # increase partials
    partials += 1

    # pause the cycle for 200 ms
    sleep(200)
