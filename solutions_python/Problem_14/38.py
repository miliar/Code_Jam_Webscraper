import math

def check_triangle(a,b,c,target):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    area = abs((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))
    return area == target

def enum_triangles(N,M,target):
    N += 1
    M += 1
    x1 = 0
    y1 = 0
    for x2 in range(N):
        for x3 in range(N):
            for y2 in range(M):
                for y3 in range(M):
                    if check_triangle((x1,y1),(x2,y2),(x3,y3),target):
                        return "%d %d %d %d %d %d" % (x1,y1,x2,y2,x3,y3)
    return "IMPOSSIBLE"


def handle_line(line):
    params = [int(x) for x in line.split()]
    return enum_triangles(params[0],params[1],params[2])


import sys
import psyco
psyco.full()

lines = open(sys.argv[1]).readlines()
num_cases = int(lines[0])
lines = lines[1:]
assert(len(lines) == num_cases)
for i,l in enumerate(lines):
    print "Case #%d: %s" % (i+1,handle_line(l))

