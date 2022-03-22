import numpy as np
import time
import math
import matplotlib.pyplot as plt


def Obstaclecheck_Circle(x, y, r, c):
    if ((y - 185) ** 2) + ((x - 300) ** 2) < (40 + c + r) ** 2:
        return True
    else:
        return False


def Obstaclecheck_Heaxgon(x, y, r, c):
    h1 = (y - r - c) - 0.577 * (x + r + c) - 24.97
    h2 = (y - r - c) + 0.577 * (x - r - c) - 255.82
    h3 = (x - r - c) - 235
    h6 = (x + r + c) - 165
    h5 = (y + r + c) + 0.577 * (x + r + c) - 175
    h4 = (y + r + c) - 0.577 * (x - r - c) + 55.82

    if (h1 < 0 and h2 < 0 and h3 < 0 and h4 > 0 and h5 > 0 and h6 > 0):
        return True
    else:
        return False


def Obstaclecheck_Polygon(x, y, r, c):
    s1 = (y - r - c) - ((0.316) * (x + r + c)) - 173.608
    s2 = (y + r + c) + (1.23 * (x + r + c)) - 229.34
    s3 = (y - r - c) + (3.2 * (x - r - c)) - 436
    s4 = (y + r + c) - 0.857 * (x - r - c) - 111.42
    s5 = y + (0.1136 * x) - 189.09

    if ((s1 < 0 and s5 > 0 and s4 > 0) or (s2 > 0 and s5 < 0 and s3 < 0)):
        return True
    else:
        return False


def Obstacle_Check(x, y, r, c):
    if Obstaclecheck_Circle(x, y, r, c):
        return True

    elif Obstaclecheck_Heaxgon(x, y, r, c):
        return True

    elif Obstaclecheck_Polygon(x, y, r, c):
        return True

    else:
        return False


map = np.full((250*2,400*2),0)
def my_map(width,height,r,c):

    for x in range(0, width*2):
        for y in range(0, height*2):
            c_x = x*0.5
            c_y = y*0.5
            s1 = (c_y - r - c) - ((0.316) * (c_x + r + c)) - 173.608
            s2 = (c_y + r + c) + (1.23 * (c_x + r + c)) - 229.34
            s3 = (c_y - r - c) + (3.2 * (c_x - r - c)) - 436
            s4 = (c_y + r + c) - 0.857 * (c_x - r - c) - 111.42
            s5 = c_y + (0.1136 * c_x) - 189.09
            h1 = (c_y - r - c) - 0.577 * (c_x + r + c) - 24.97
            h2 = (c_y - r - c) + 0.577 * (c_x - r - c) - 255.82
            h3 = (c_x - r - c) - 235
            h6 = (c_x + r + c) - 165
            h5 = (c_y + r + c) + 0.577 * (c_x + r + c) - 175
            h4 = (c_y + r + c) - 0.577 * (c_x - r - c) + 55.82
            if ((c_y - 185) ** 2) + ((c_x - 300) ** 2) < (40 + c + r) ** 2:
                map[round(y),round(x)] = 1
            elif ((s1 < 0 and s5 > 0 and s4 > 0) or (s2 > 0 and s5 < 0 and s3 < 0)):
                map[round(y),round(x)] = 1
            elif (h1 < 0 and h2 < 0 and h3 < 0 and h4 > 0 and h5 > 0 and h6 > 0):
                map[round(y),round(x)] = 1
    return map


def my_map2(width,height):

    for x in range(0, width*2):
        for y in range(0, height*2):
            c_x = x*0.5
            c_y = y*0.5
            s1 = (c_y) - ((0.316) * (c_x)) - 173.608
            s2 = (c_y) + (1.23 * (c_x )) - 229.34
            s3 = (c_y) + (3.2 * (c_x)) - 436
            s4 = (c_y) - 0.857 * (c_x) - 111.42
            s5 = c_y + (0.1136 * c_x) - 189.09
            h1 = (c_y) - 0.577 * (c_x) - 24.97
            h2 = (c_y) + 0.577 * (c_x) - 255.82
            h3 = (c_x) - 235
            h6 = (c_x) - 165
            h5 = (c_y) + 0.577 * (c_x) - 175
            h4 = (c_y) - 0.577 * (c_x) + 55.82
            if ((c_y - 185) ** 2) + ((c_x - 300) ** 2) < (40) ** 2:
                map[round(y),round(x)] = 1
            elif ((s1 < 0 and s5 > 0 and s4 > 0) or (s2 > 0 and s5 < 0 and s3 < 0)):
                map[round(y),round(x)] = 1
            elif (h1 < 0 and h2 < 0 and h3 < 0 and h4 > 0 and h5 > 0 and h6 > 0):
                map[round(y),round(x)] = 1
    return map



def moveForward(current_node,step):
    new_node = threshold(current_node[0] + step * math.cos(math.radians(current_node[2])),
                    current_node[1] + step * math.sin(math.radians(current_node[2])), current_node[2])
    if not inbounds(new_node[0], new_node[1]) or map[to_region(new_node[1], new_node[0])] == 1:
        return False
    else:
        return new_node


def to_region(y,x):
    return round(y*2), round(x*2)

def moveUp30(current_node,step):
    new_node = threshold(
        current_node[0] + step * math.cos(math.radians(current_node[2] + 30)),
        current_node[1] + step * math.sin(math.radians(current_node[2] + 30)),
        current_node[2] + 30)
    if not inbounds(new_node[0],new_node[1]) or map[to_region(new_node[1], new_node[0])] == 1:
        return False
    else:
        return new_node


def moveUp60(current_node,step):
    new_node = threshold(current_node[0] + step * math.cos(math.radians(current_node[2] + 60)),
                    current_node[1] + step * math.sin(math.radians(current_node[2] + 60)), current_node[2] + 60)
    if not inbounds(new_node[0], new_node[1]) or map[to_region(new_node[1], new_node[0])] == 1:
        return False
    else:
        return new_node


def moveDown30(current_node,step):
    new_node = threshold(current_node[0] + step * math.cos(math.radians(current_node[2] + 330)),
                    current_node[1] + step * math.sin(math.radians(current_node[2] + 330)), current_node[2] + 330)
    if not inbounds(new_node[0], new_node[1]) or map[to_region(new_node[1], new_node[0])] == 1:
        return False
    else:
        return new_node


def moveDown60(current_node,step):
    new_node = threshold(current_node[0] + step * math.cos(math.radians(current_node[2] + 300)),
                    current_node[1] + step * math.sin(math.radians(current_node[2] + 300)), current_node[2] + 300)
    if not inbounds(new_node[0], new_node[1]) or map[to_region(new_node[1], new_node[0])] == 1:
        return False
    else:
        return new_node

def threshold(x, y, th):
    x = (round(x * 2)/2)
    y = (round(y * 2)/2)
    th = (round(th / 30) % 12)

    return x, y, th


def get_valid_neighbors(current_node,step):
    neighbors = []
    for next_function in [moveForward,moveUp30,moveDown60,moveDown30,moveUp60]:
        result = next_function(current_node,step)
        if result == False:
            continue
        neighbors.append(result)

    return neighbors

def inbounds(x,y):
    return 0 <= x < map.shape[1]/2 and 0 <= y < map.shape[0]/2

map = my_map(400,250,1,1)
map2 = my_map2(400,250)
def A_star(start_node,goal_node,step):
    paths = {}
    open_list = []
    open_list.append((start_node,float('inf')))
    while open_list:
        open_list.sort(key=lambda k: k[1])
        current_node, dist = open_list.pop(0)
        if dist <= 1.5:
            goal_node = current_node
            break
        neighbors = get_valid_neighbors(current_node, step)
        for node in neighbors:
            dist = math.dist(node[:2],goal_node[:2])
            if map[to_region(node[1], node[0])] == 1:
                continue
            open_list.append((node,dist))
            #map[to_region(node[1], node[0])] = 200
            map2[to_region(node[1], node[0])] = 200
            plot()
            paths[node] = current_node
    current_node = goal_node
    path = []
    while current_node != start_node:
        current_node = paths[current_node]
        path.append(current_node)
    return path


img = plt.imshow(map2[::2,::2])
ax = plt.gca()
ax.invert_yaxis()
def plot():
    img.set_data(map2[::2,::2])
    plt.pause(0.0000000000000000000000000000000000000000000000000000000000000000000000000001)

r = int(input('Please enter the radius of the robot: '))
c = int(input('Please enter the clearance value: '))
step = int(input('Please enter the step size: '))


a1,b1,c1 = input("Enter the co-ordinates for the start node: ").split(",",3)
start_node = tuple([int(a1),int(b1),int(c1)])
while map[int(b1),int(a1)] == 1:
    print('This is in the obstacle space: ')
    a1, b1, c1 = input("Enter the co-ordinates for the start node: ").split(",", 3)

a2,b2,c2 = input("Enter the co-ordinates for the goal node: ").split(",",3)
goal_node = tuple([int(a2),int(b2),int(c2)])
while map[int(b2),int(a2)] == 1:
    print('This is in the obstacle space: ')
    a2, b2, c2 = input("Enter the co-ordinates for the goal node: ").split(",", 3)

result = A_star(start_node,goal_node,step)
for x,y,_ in result:
    map[to_region(y, x)] = 100
    plot()


