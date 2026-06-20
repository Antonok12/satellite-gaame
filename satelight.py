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
start_time=time.time()

def draw():
    global total_time
    screen.blit("space",(0,0))
    number=1
    for stat in stats:
        screen.draw.text(str(number),(stat.pos[0],stat.pos[1]+15))
        stat.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,0,200))
    if next_stat<8:
        total_time=time.time()-start_time
        screen.draw.text(str(round(total_time,1)),(0,0),fontsize=30)
    else:
        screen.draw.text("you won in "+str(round(total_time,1))+" seconds!!!",(170,300),fontsize=50)
def update():
    pass

def on_mouse_down(pos):
    global next_stat,lines
    if next_stat<8:
        if stats[next_stat].collidepoint(pos):
            if next_stat:
                lines.append((stats[next_stat-1].pos,stats[next_stat].pos))
            next_stat=next_stat+1
        else:
            lines=[]
            next_stat=0
            


pgzrun.go()
