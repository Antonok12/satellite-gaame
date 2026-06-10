import pgzrun
import random
import time
HEIGHT= 600
WIDTH=800
stats=[]
lines=[]
next_stat=0

start_time=0
total_time=0
end_time=0

number_of_satellite=8
for i in range(8):
    stat=Actor("stat")
    x=random.randint(10,710)
    y=random.randint(10,590)
    stat.pos=(x,y)
    stats.append(stat)

def draw():
    screen.blit("space",(0,0))
    number=1
    for stat in stats:
        screen.draw.text(str(number),(stat.pos[0],stat.pos[1]+15))
        stat.draw()
        number=number+1

def update():
    pass

def on_mouse_down(pos):
    global next_stat,lines
    if next_stat<8:
        if stats[next_stat].collidepoint(pos):
            next_stat=next_stat+1
            


pgzrun.go()