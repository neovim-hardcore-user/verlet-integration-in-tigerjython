from gturtle import *
import time
from math import *
from collections import defaultdict

points = []


point_radius = 10

def length(x, y):
    return sqrt(x**2+y**2)




def update_point(point):
    if not point[4]:
        vel = [point[0] - point[2], point[1] - point[3]-0.001]
         
        point[2] = point[0]
        point[3] = point[1]


        point[0] += vel[0]
        point[1] += vel[1]

        
    

    if point[0] < -500+point_radius:
        point[0] = -500+point_radius

    if point[0] > 500-point_radius:
        point[0] = 500-point_radius
        
    if point[1] > 500-point_radius:
        point[1] = 500-point_radius
        
    if point[1] < -500+point_radius:
        point[1] = -500+point_radius



def point_collision(f, p1, objects):
    for i in objects:
        if i != f:
            p2 = points[i]
            if p1[0]+point_radius*4 >= p2[0] and p1[1]+point_radius*4 >= p2[1]:
                d = [p1[0]-p2[0], p1[1]-p2[1]]

                l = length(d[0], d[1])


                if l <= point_radius*2 and l != 0:
                    ld = (l-point_radius*2)/2/l*(p2[4]+p1[4]+1)


                    if not p2[4]:
                        p2[0] += d[0]*ld
                        p2[1] += d[1]*ld

                    if not p1[4]:
                        p1[0] -= d[0]*ld
                        p1[1] -= d[1]*ld

grid_dict = defaultdict(list)

for x in range(40):
    for y in range(20):
        points.append([x*point_radius*2+point_radius, y*point_radius*2+point_radius, x*point_radius*2+point_radius+y*0.01, y*point_radius*2+point_radius, False])
        
print(len(points))
    
makeTurtle()
speed(-1)
hideTurtle()

p = getPlayground()
p.enableRepaint(False)

        
        
while True:
    for i in range(5):
        grid_dict.clear()

        for point in points:
            update_point(point)

        for i, point in enumerate(points):
            grid_dict[int(point[0]/(point_radius*2)), int(point[1]/(point_radius*2))].append(i)


        for i, point in enumerate(points):
            c = [int(point[0]/(point_radius*2)), int(point[1]/(point_radius*2))]
            
            point_collision(i, point,  grid_dict[c[0], c[1]]     +
                                       grid_dict[c[0]-1, c[1]-1] +
                                       grid_dict[c[0], c[1]-1]   +
                                       grid_dict[c[0]+1, c[1]-1] +
                                       grid_dict[c[0]+1, c[1]]   +
                                       grid_dict[c[0]+1, c[1]+1] +
                                       grid_dict[c[0], c[1]+1]   + 
                                       grid_dict[c[0]-1, c[1]+1] +
                                       grid_dict[c[0]-1, c[1]])

    p.clear()

    for point in points:
        setPos(point[0], point[1])
        dot(point_radius*2)
    p.repaint()
