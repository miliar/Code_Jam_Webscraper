# python 3
import string
import itertools
import sys
from heapq import *

def cut_pieces(x, tab):
    result = []
    a = []
    for (b, e, w) in tab:
        heappush(a, (b, 1, w))
        heappush(a, (e, -1, w))
    wspeeds = [0]
    speed = 0
    last_dist = 0
    while len(a) > 0:
        (dist, val, ws) = heappop(a)
        if dist > last_dist:
            result.append((speed, dist-last_dist))
            last_dist = dist
        if val > 0:
            wspeeds.append(ws)
            if ws > speed:
                speed = ws
        else:
            wspeeds.remove(ws)
            speed = max(wspeeds)
    if last_dist < x:
        result.append((0, x-last_dist))
    return result

def process_case(x, s, r, t, n, tab):
    pieces = cut_pieces(x, tab)
    pieces.sort()
    result = 0
    for (speed, dist) in pieces:
        pt = dist / (speed + s)
        if t > 0:
            if t * (speed + r) >= dist:
                pt = dist / (speed + r)
                t -= pt
            else:
                d1 = t * (speed + r)
                d2 = dist - d1
                pt = t + d2 / (speed + s)
                t = 0
        result += pt
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        print(ci)
        x, s, r, t, n = line_of_numbers(next(lines))
        tab = [line_of_numbers(next(lines)) for i in range(n)]
        result = process_case(x, s, r, t, n, tab)
        yield 'Case #{0}: {1}\n'.format(ci, result)
    
def line_of_numbers(s):
    return [int(sub) for sub in s.split()]

def input_gen(f_in):
    for line in f_in:
        if line.endswith('\n'):
            line = line[:-1]
        yield line

def start(basename):
    infile = basename + '.in'
    outfile = basename + '.out'
    f_in = open(infile, 'r')
    f_out = open(outfile, 'w')
    f_out.writelines(result_gen(input_gen(f_in)))
    f_in.close()
    f_out.close()

##start('A-test')
##start('A-small-attempt0')
start('A-large')
