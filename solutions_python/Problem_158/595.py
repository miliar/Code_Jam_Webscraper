__author__ = 'dkopiychenko'

import os

def winner(x, r, c):
    if x == 1: return 'GABRIEL'
    if x == 2:
        if r*c % 2 == 0:
            return 'GABRIEL'
        else: return 'RICHARD'
    if x == 3:
        if r*c % 3 != 0 or r < 2 or c < 2:
            return 'RICHARD'
        else: return 'GABRIEL'
    if x == 4:
        if r < 3 or c < 3 or r*c == 9:
            return 'RICHARD'
        else: return 'GABRIEL'


with open(os.path.expanduser("~/gcj2015/input04.txt")) as f:
    n = f.readline().strip('\n')
    print n
    lines = [x.strip('\n') for x in f.readlines()]
    counter = 1
    for l in lines:
        x, r, c = [int(g) for g in l.split(' ')]
        print 'Case #' + str(counter) + ': ' + winner(x,r,c)
        counter += 1

