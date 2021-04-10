import random
from pykkar import *

f = open("room.txt")

room = []
i = 0

while True:
    line = f.readline()
    if line == "":
        break
    row = []
    for tile in line:
        if tile != "\n":
            row += [tile]
    room.insert(i,row)
    i += 1
    
f.close()

height = len(room)
width = len(room[0])

directions = ["^",">","v","<"]

r = random.randint(0,3)

while True:
    x = random.randint(1, width-2)
    y = random.randint(1, height-2)
    if room[y][x] != "#":
        room[y][x] = directions[r]
        break
    
world = ""

for row in room:
    line = ""
    for tile in row:
        line += tile
    line += "\n"
    world += line

create_world("" + world + "")
current_x, current_y = (0,0)
painted_cordinates = []
def set_direction(direction):    
    if direction == "N":
        return (0, 1)
    elif direction == "S":
        return (0, -1)
    elif direction == "W":
        return (-1, 0)
    elif direction == "E":
        return (1, 0)
    
repeat_the_step = 4
indentation_for_the_func = 1
def step_saver():
    
    global current_x, current_y
    current_x += set_direction(get_direction())[0]
    current_y += set_direction(get_direction())[1]
    
    step()
def paint_saver():
    paint()
    cordinates = (current_x, current_y)
    painted_cordinates.append(cordinates)
def back():
    right()
    right()
def main_func():
    back()
    step_saver()
    back()
def check(state):
    if state == True:
        return
def func_bottom():
    step_saver()    
    pukkar_fill()        
    main_func()
def pukkar_fill():
    check(is_painted())
    
    paint_saver()
    
    for the_step in range(repeat_the_step):
        
        for indentation in range(indentation_for_the_func):
            
            if is_wall():
                continue
            
            global current_x, current_y, painted_cordinates
            
            print(set_direction(get_direction())[0],set_direction(get_direction())[1])
            
            cordinates = (current_x + set_direction(get_direction())[0], current_y + set_direction(get_direction())[1])
                    
            if cordinates in painted_cordinates:
                continue 
                    
            func_bottom()
            
        right()

pukkar_fill()