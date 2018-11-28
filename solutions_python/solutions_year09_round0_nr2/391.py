#/usr/bin/python
import os
import sys

g_label = "a"

def drain(src, point, height, width):
    min_neighbor = North(point, height, width)
    for neighbor in [West(point, height, width), East(point, height, width), South(point, height, width)]:
        if not min_neighbor or ( \
           neighbor and \
           src[neighbor[0]][neighbor[1]] < \
           src[min_neighbor[0]][min_neighbor[1]]):
            min_neighbor = neighbor
    if min_neighbor and src[min_neighbor[0]][min_neighbor[1]] < src[point[0]][point[1]]:
        return min_neighbor
    return None

def paint(src, dest, point, height, width):
    global g_label
    drain_point = drain(src, point, height, width)
    if not drain_point:
        if not dest[point[0]][point[1]]:
            dest[point[0]][point[1]] = g_label
            g_label = chr(ord(g_label) + 1)

    else:
        dest[point[0]][point[1]] =  paint(src, dest, drain_point, height, width)
    return dest[point[0]][point[1]]
    

def main():
    global g_label

    fsock = file("input.txt")
    number = int(fsock.readline().strip())
    f = file ("output.txt", "w") 
    for i in range(1, number+1):
        g_label = "a"
        src = []
        dest = []
        height, width = [int(value) for value in fsock.readline().split()]
        for h in range(1, height+1):
            src.append([int(value) for value in fsock.readline().split()])
            dest.append([None for w in range(width)])

        for row in range(height):
            for col in range(width):
                if not dest[row][col]:
                    paint(src, dest, (row, col), height, width)

        
        print >>f , "Case #%s:" % i
        for row in dest:

            
            print >>f, " ".join(row)
            
def North(point, height, width):
    if point[0] - 1 < 0:
        return None
    return (point[0] -1, point[1])
def West(point, height, width):
    if point[1] -1 < 0:
        return None
    return (point[0], point[1] -1)
def East(point, height, width):
    if point[1] + 1 >= width:
        return None
    return (point[0], point[1] + 1)

def South(point, height, width):
    if point[0] + 1 >= height:
        return None
    return (point[0] + 1, point[1])

if __name__ == "__main__":
    main()
