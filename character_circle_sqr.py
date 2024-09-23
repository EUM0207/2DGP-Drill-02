import os
import math
import pico2d
os.chdir('C:\\tuk_GitHub\\2DGP-Drill-02')

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_in_square():
    
    r = 0
    while r < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + r, 90)
        r += 2
        delay(0.01)
    
    
    u = 0
    while u < 510:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(800, 90 + u)
        u += 2
        delay(0.01)
    
    
    l = 800
    while l > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(l, 590)
        l -= 2
        delay(0.01)

    
    d = 510
    while d > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0, d)
        d -= 2
        delay(0.01)

    r = 0
    while r < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(r, 90)
        r += 2
        delay(0.01)


def move_in_circle():
    CENTER_X, CENTER_Y = 400, 300
    RADIUS = 200  
    angle = 0

    while angle < 360:
        clear_canvas_now()
        grass.draw_now(400, 30)
        
        radian = math.radians(angle)
        x = CENTER_X + RADIUS * math.cos(radian)
        y = CENTER_Y + RADIUS * math.sin(radian)
        
        character.draw_now(x, y)
        
        angle += 2  
        delay(0.01)


while True:
    move_in_square()  
    move_in_circle()  

close_canvas()
