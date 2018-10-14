#! /usr/bin/python
import os
import pyximport

#pyximport.install()
#os.chdir(os.path.dirname(os.path.abspath(__file__)))


#from ExtSolve import *

inf = open('input.in')
inp = inf.read().split('\n')
inf.close()

def Solve(*args):
    R, C, grid = args
    change = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 4:
                continue
            elif grid[i][j] == 0:
                if filter(lambda x:grid[x][j]<4,range(0,i)):
                    continue
                elif len(filter(lambda x:x != j and grid[i][x]<4,range(C)))>0 or \
                    len(filter(lambda x:grid[x][j]<4,range(i+1,R)))>0:
                    change += 1
                else:
                    print j
                    change = -1
            elif grid[i][j] == 1:
                if filter(lambda x:grid[i][x]<4,range(j+1,C)):
                    continue
                elif len(filter(lambda x:x != i and grid[x][j]<4,range(R)))>0 or \
                    len(filter(lambda x:grid[i][x]<4,range(0,j)))>0:
                    change += 1
                else:
                    print j
                    change = -1
            elif grid[i][j] == 2:
                if filter(lambda x:grid[x][j]<4,range(i+1,R)):
                    continue
                elif len(filter(lambda x:x != j and grid[i][x]<4,range(C)))>0 or \
                    len(filter(lambda x:grid[x][j]<4,range(0,i)))>0:
                    change += 1
                else:
                    print j
                    change = -1
            else:
                if filter(lambda x:grid[i][x]<4,range(0,j)):
                    continue
                elif len(filter(lambda x:x != i and grid[x][j]<4,range(R)))>0 or \
                    len(filter(lambda x:grid[i][x]<4,range(j+1,C)))>0:
                    change += 1
                else:
                    print j
                    change = -1
        if change < 0:
            print i
            break
    if change < 0:
        return 'IMPOSSIBLE'
    else:
        return change

T = int(inp.pop(0))
outf = open('output','w')
for i in range(T):
    r, c = [int(x) for x in inp.pop(0).split(' ')]
    grid = list()
    for j in range(0,r):
        row = inp.pop(0)
        arrows = list()
        for k in range(0,c):
            arrows += [['^','>','v','<','.'].index(row[k])]
        grid += [arrows]
    outf.write('Case #%d: %s\n'%(i+1,Solve(r, c, grid)))
outf.close()