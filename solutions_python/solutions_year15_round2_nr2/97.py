from math import sqrt, pow, log, ceil, log10, floor
from sys import stdin, setrecursionlimit
import copy
import random

setrecursionlimit(100000)
debug = 0

def happyness(array, R, C):
    
    h = 0

    for x in range(R):
        for y in range(C):
            if x + 1 < R: 
                if array[x][y] == array[x + 1][y] and array[x][y] == 1:
                    h = h + 1
            if y + 1 < C: 
                if array[x][y] == array[x][y + 1] and array[x][y] == 1:
                    h = h + 1

    return h

def solve(R, C, N):

    h = 10000000000000000
    triesMax = 100000

    for tries in range(triesMax):
        array = [[0 for x in range(C)] for y in range(R)]
        nb = 0

        while nb < N:

            x = random.randint(0, R - 1)
            y = random.randint(0, C - 1)

            if array[x][y] == 0:
                array[x][y] = 1
                nb += 1

        h = min(h, happyness(array, R, C))

        if h == 0:
            triesMax = 1
        elif h == 1:
            triesMax = 1000

    return h

T = int(stdin.readline())

for i in range(1,T+1):
    
    R, C, N, = map(int, stdin.readline().split(' '))
    
    print "Case #" + str(i) + ":", 

    if debug:
        print
        print R, C, N

    rep = solve(R, C, N)

    print rep


# x | x
# -   -
# x | x
# -   -
# x | x

