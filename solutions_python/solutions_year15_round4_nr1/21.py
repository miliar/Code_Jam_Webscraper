#!/usr/bin/python


import sys
import math
import numpy as np
import time
#import multiprocessing

def readline():
    return sys.stdin.readline().strip()

def readints():
    return [int(x) for x in readline().split()]

# print 14
# for i in range(14):
#     x = min(3000, 300 * (i+1))
#     print x
#     for i in range(x):
#         print np.random.randint(0,200000),np.random.randint(0,200000)
# exit()

tstart = time.clock()



# NOTE: apparently need to make sure this stuff is seperated
if __name__ == '__main__':
    T, = readints()
    for testcase in range(T):

        R,C = readints()

        grid = []

        for ridx in range(R):
            line = readline()
            row = []
            # for ch in line:
            #     {'<':0}
            grid.append(line)

        def trydir(x,y,dir):  # dir = 0,3
            # true if hits an arrow
            if dir == '<':
                while True:
                    x -= 1
                    if x < 0:
                        return False
                    if grid[y][x] != '.':
                        return True
            elif dir == '^':
                while True:
                    y -= 1
                    if y < 0:
                        return False
                    if grid[y][x] != '.':
                        return True
            elif dir == 'v':
                while True:
                    y += 1
                    if y >= R:
                        return False
                    if grid[y][x] != '.':
                        return True
            elif dir == '>':
                while True:
                    x += 1
                    if x >= C:
                        return False
                    if grid[y][x] != '.':
                        return True
            else:
                assert False
            

        def solve():
            ret = 0
            for y in range(R):
                row = grid[y]
                #print "y %d row %s" % (y, row)
                for x in range(C):
                    ch = row[x]
                    if ch == '.':
                        continue
                    if trydir(x,y, ch):
                        continue
                    for dir in '<>v^':
                        if trydir(x,y,dir):
                            ret += 1
                            break
                    else:
                        return 'IMPOSSIBLE'
            return '%d' % ret

        print "Case #%d: %s" % ( testcase+1, solve())



#print "done in ",  time.clock() - tstart
