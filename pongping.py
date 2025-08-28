from pygame import *


width = 600
height = 500

window = display.set_mode((width, height))
display.set_caption('Pong-Ping Not For All')


bcakground_color = (92, 214, 115)
window.fill(bcakground_color)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(bcakground_color)
    display.update()
