import pygame #as pg
import random #as rd
import math
import time
from pygame.color import THECOLORS
random.seed()
iteration = 1000000
WHITE = (255, 255, 255)
color_of_point = 'black'
color_of_pixels = 'white'
point_radius = 1
pygame.init()
pygame.mixer.init()
res = WIDTH, HEIGHT=1000,720
screen = pygame.display.set_mode(res, pygame.SCALED)
screen.fill(THECOLORS['black'])
clock = pygame.time.Clock()
side_of_triangle = 600
list_of_points = []
def draw_triangl():
    height_of_triangle = side_of_triangle*math.sqrt(3)/2
    #pointA
    a_coordinate_x = WIDTH/4
    a_coordinate_y = HEIGHT-HEIGHT/4
    pygame.draw.rect(screen, THECOLORS[color_of_point], (a_coordinate_x, a_coordinate_y, 10, 10), 0)
    #pointB
    b_coordinate_x = a_coordinate_x+side_of_triangle/2
    b_coordinate_y = a_coordinate_y-height_of_triangle
    pygame.draw.rect(screen, THECOLORS[color_of_point], (b_coordinate_x, b_coordinate_y, 10, 10), 0)
    #pointC
    c_coordinate_x = a_coordinate_x+side_of_triangle
    c_coordinate_y = a_coordinate_y
    pygame.draw.rect(screen, THECOLORS[color_of_point], (c_coordinate_x, c_coordinate_y, 10, 10), 0)
    start_point_coordinates = ((a_coordinate_x+b_coordinate_x)/2, (a_coordinate_y+b_coordinate_y)/2)
    list_of_points.append(start_point_coordinates)
    previous_point_coordinates = start_point_coordinates
    for i in range(iteration):
        point = random.randint(1,3)
        if point == 1:#A
            new_coordinates = ((previous_point_coordinates[0]+a_coordinate_x)/2, (previous_point_coordinates[1]+a_coordinate_y)/2)
            previous_point_coordinates = new_coordinates
        elif point == 2:#B
            new_coordinates = ((previous_point_coordinates[0]+b_coordinate_x)/2, (previous_point_coordinates[1]+b_coordinate_y)/2)
            previous_point_coordinates = new_coordinates
        else:#C
            new_coordinates = ((previous_point_coordinates[0]+c_coordinate_x)/2, (previous_point_coordinates[1]+c_coordinate_y)/2)
            previous_point_coordinates = new_coordinates
        list_of_points.append(new_coordinates)
def draw(list_of_points_):
    for point in list_of_points_:
        pygame.draw.circle(screen, THECOLORS[color_of_pixels], point, point_radius, 0)
def run():
    print("Calculation test start")
    start_calculation = time.time()
    #calculation
    draw_triangl()
    stop_calculation = time.time()
    print("Writing test start")
    #write
    with open('list_of_points.txt','w') as f:
        str_list = []
        for el in list_of_points:
            temp=''
            for e in el:
                temp+=str(e)
                temp+=','
            str_list.append(temp)
        start_writing = time.time()
        f.write("\n".join(str_list))
    stop_writing = time.time()
    print("Reading test start")
    start_reading = time.time()
    #read    
    with open('list_of_points.txt','r') as f:
        from_file_read_list = f.read().split("\n")
        stop_reading = time.time()
        read_list = []
        for el in from_file_read_list:
            temp = el.split(",")
            temp.remove('')
            temp_temp = tuple(float(i) for i in temp)
            read_list.append(temp_temp)
    f.close()
    print("Drawing test start")
    start_draw = time.time()
    draw(read_list)
    #draw
    pygame.display.update()
    #pygame.display.flip()
    stop_draw = time.time()
    print("calculation          writing           reading                draw")
    return stop_calculation-start_calculation, stop_writing-start_writing, stop_reading-start_reading, stop_draw-start_draw
    #pygame.quit()
if __name__ == "__main__":
    print(run())