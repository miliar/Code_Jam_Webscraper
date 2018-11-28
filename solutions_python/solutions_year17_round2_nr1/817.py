from sys import *
from math import *

def calc_max_speed(d, h):
    hp = h[0]
    hv = h[1]
    t = (d-hp)/hv
    return d/t


def calc_speed(d, horses):
    max_speed = -1
    for h in horses:
        ms = calc_max_speed(d, h)
        if max_speed == -1 or ms < max_speed:
            max_speed = ms
    print(max_speed)
    return str(max_speed) + "\n"


fin = open(argv[1] + ".in", 'r') 
fout = open(argv[1] + ".out", 'w')
    
ncases = int(fin.readline())
for ci in range(0, ncases):
    (d,n) = tuple([int(x) for x in fin.readline().split()])
    horses = []
    for i in range(n):
        horses.append(tuple([int(x) for x in fin.readline().split()]))
    result = calc_speed(d, horses)
    fout.write("Case #" + str(ci+1) + ": " + result)

fin.close()
fout.close()

