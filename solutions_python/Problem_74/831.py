"""
From Daniel Herde
daniel@dher.de

uses: scipy library

usage: python solution.py file.in > file.out
"""

import sys
import scipy

path = sys.argv[1]
# path = 'test.txt'

def parse():
    
    file = open(path,'r')
    data = file.readlines()
    file.close()

    for line in data[1:]:
        robots={'O':[], 'B':[]}
        rpos={'O':1, 'B':1}
    
        for i,element in enumerate(line.split(' ')[1:]):
            if element=='O':
                state = 'O'
            elif element=='B':
                state = 'B'
            else:
                robots[state].append([abs(int(element)-rpos[state]),i/2])
                rpos[state]=int(element)        
 
        robots['O'].append([0,-10])
        robots['B'].append([0,-10])
        yield robots, i/2+1

def totaltime(robots, time):
    t = 0
    for i in range(time):

        if robots['O'][0][1] == i:
           timestep = robots['O'].pop(0)[0]+1
           robots['B'][0][0] = max(robots['B'][0][0]-timestep,0)
           t += timestep
        else:
           timestep = robots['B'].pop(0)[0]+1
           robots['O'][0][0] = max(robots['O'][0][0]-timestep,0)
           t += timestep

    return t

    
for i,data in enumerate(parse()):
    print 'Case #'+str(i+1)+': '+str(totaltime(*data))
