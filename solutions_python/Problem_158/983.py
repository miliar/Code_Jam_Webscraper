# Written in Python 3.x

import math
import sys
from math import sqrt


def solve_omni(grid_x,grid_y,omini_size):
    
    # if grid not multiple size of omni
    if(divmod(grid_x * grid_y, omini_size)[1] != 0):
        return "RICHARD"

    if(sqrt(omini_size) > grid_y):
        return "RICHARD"

    if(omini_size == 4 and grid_y == 2):
        return "RICHARD"


    return "GABRIEL"

op = {}

op[(1,1,1)] = 'GABRIEL'
op[(1,2,1)] = 'GABRIEL'
op[(1,3,1)] = 'GABRIEL'
op[(1,4,1)] = 'GABRIEL'
op[(1,2,2)] = 'GABRIEL'
op[(1,3,2)] = 'GABRIEL'
op[(1,4,2)] = 'GABRIEL'
op[(1,3,3)] = 'GABRIEL'
op[(1,4,3)] = 'GABRIEL'
op[(1,4,4)] = 'GABRIEL'
op[(2,1,1)] = 'RICHARD'
op[(2,2,1)] = 'GABRIEL'
op[(2,3,1)] = 'RICHARD'
op[(2,4,1)] = 'GABRIEL'
op[(2,2,2)] = 'GABRIEL'
op[(2,3,2)] = 'GABRIEL'
op[(2,4,2)] = 'GABRIEL'
op[(2,3,3)] = 'RICHARD'
op[(2,4,3)] = 'GABRIEL'
op[(2,4,4)] = 'GABRIEL'
op[(3,1,1)] = 'RICHARD'
op[(3,2,1)] = 'RICHARD'
op[(3,3,1)] = 'RICHARD'
op[(3,4,1)] = 'RICHARD'
op[(3,2,2)] = 'RICHARD'
op[(3,3,2)] = 'GABRIEL'
op[(3,4,2)] = 'RICHARD'
op[(3,3,3)] = 'GABRIEL'
op[(3,4,3)] = 'GABRIEL'
op[(3,4,4)] = 'RICHARD'
op[(4,1,1)] = 'RICHARD'
op[(4,2,1)] = 'RICHARD'
op[(4,3,1)] = 'RICHARD'
op[(4,4,1)] = 'RICHARD'
op[(4,2,2)] = 'RICHARD'
op[(4,3,2)] = 'RICHARD'
op[(4,4,2)] = 'RICHARD'
op[(4,3,3)] = 'RICHARD'
op[(4,4,3)] = 'GABRIEL'
op[(4,4,4)] = 'GABRIEL'




fidi = open('D-small-attempt2.in','r')
#fidi = open('test.in','r')

fido = open('test.out','w')

T = fidi.readline()
T = int(T)

for t in range(T):
    c = [int(i) for i in fidi.readline().split()]
    omini_size = c[0]
    grid_x = c[1]
    grid_y = c[2]
    if (grid_x < grid_y):
        grid_tmp = grid_x
        grid_x = grid_y
        grid_y = grid_tmp

    #ans = solve_omni(grid_x,grid_y,omini_size)
    ans = op[(omini_size,grid_x,grid_y)]
    print('Case #%d: ' % (t+1), "%s" % ans)
    fido.write('Case #%d: ' % (t+1) + '%s' % ans + '\n')

fidi.close()
fido.close()
