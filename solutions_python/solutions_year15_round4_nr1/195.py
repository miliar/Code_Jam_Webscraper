# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:24:10 2015

@author: peter
"""
#%% import and start up

import numpy as np

IN_MAIN = (__name__ == "__main__")
PB_NAME = 'A'

EMPTY = 0
RIGHT = 1
UP = 2
LEFT = 3
DOWN = 4

char_to_byte = {'.':EMPTY, '>':RIGHT, '^':UP, '<':LEFT, 'v':DOWN}

#%% IO
def read_input(fin_name):
    with open(fin_name, 'r') as fin:
        nb_cases = int(fin.readline())
        for _ in xrange(nb_cases):
            r, c = map(int, fin.readline().split())
            land = np.zeros((r,c), dtype=np.byte)
            for row in xrange(r):
                chars = fin.readline().strip()
                land[row, :] = map(lambda x: char_to_byte[x], chars)
            yield (r, c, land)

def runit(fin_name, fout_name):
    with open(fout_name, 'w') as fout:
        for i, case in enumerate(read_input(fin_name), 1):
            fout.write('Case #{}: {}\n'.format(i, proceed(case)))
            
            
#%% proceed


def proceed(case):
    (r,c,land) = case
#    print case
    count = 0
    for i in xrange(r):
        for j in xrange(c):
#            print count
#            print i, j
            direction = land[i, j]
            if direction == EMPTY:
#                print 'continue'
                continue
            have_other = ((np.sum(land[i, :]) + np.sum(land[:, j])) > 2*direction)
            if not have_other:
#                print 'out'
                return 'IMPOSSIBLE'
            if direction == RIGHT:
                if j == c-1 or np.sum(land[i, (j+1):]) == 0:
                    count += 1
            elif direction == UP:
                if i == 0 or np.sum(land[:i, j]) == 0:
                    count += 1    
            elif direction == LEFT:
                if j == 0 or np.sum(land[i, :j]) == 0:
                    count += 1              
            elif direction == DOWN:
                if i == r-1 or np.sum(land[(i+1):, j]) == 0:
                    count += 1
    return count


#%% run small set
ATTEMPT = 0;
filename = '{}-small-attempt{}'.format(PB_NAME, ATTEMPT);
runit(filename + '.in', filename + '.out')

#%% run big set
filename = '{}-large'.format(PB_NAME);
runit(filename + '.in', filename + '.out')


#%% run in command line

def main(args):
    runit(args[0], args[1])

if IN_MAIN:
    import sys
    main(sys.argv[1:])
    