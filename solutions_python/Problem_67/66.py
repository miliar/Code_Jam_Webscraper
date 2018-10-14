#!/usr/bin/env python
#By Jai Dhyani

import math, sys, os

def getints(f):
    return [int(x) for x in f.readline().split()]

def solve( f ):
    num_rec = getints(f)[0]
    recs = [[] for i in xrange(num_rec)]
    max_x=max_y=0
    for i in xrange(num_rec):
        recs[i]=getints(f)
        if recs[i][2]>max_x:
            max_x=recs[i][2]
        if recs[i][3]>max_y:
            max_y=recs[i][3]
    grid = [ [0 for x in xrange(max_x+1)] for y in xrange(max_y+1) ]
    for r in recs:
        for y in xrange(r[1],r[3]+1):
            for x in xrange(r[0],r[2]+1):
                grid[y][x] = 1
    turns=0
    while simulate(grid):
        turns+=1
    print turns
    return turns

def simulate( grid ):
    n_rows = len(grid)
    n_cols = len(grid[0])
    turn_off = []
    turn_on = []
    is_alive=False
    for y in xrange(n_rows):
        for x in xrange(n_cols):
            if grid[y][x]:
                is_alive=True
            if grid[y][x]==1 and (y==0 or grid[y-1][x]==0) and (x==0 or grid[y][x-1]==0):
                turn_off.append((x,y))
            elif grid[y][x]==0 and (y!=0 and grid[y-1][x]==1) and (x!=0 and grid[y][x-1]==1):
                turn_on.append((x,y))
    for (x,y) in turn_on:
        grid[y][x]=1
    for (x,y) in turn_off:
        grid[y][x]=0
    return is_alive

if __name__ == '__main__':
    filenames = [f for f in os.listdir('.') if f[-2:]=='in']
    for filename in filenames:
        outname=filename+'.out'
        f=open(filename)
        out=open(outname,'w')
        try:
            numtrials = getints(f)[0]
        except IndexError as ie:
            print 'no input data in %s'%filename
            exit(0)
        for i in xrange(numtrials):
            answer_num = solve(f)
            answer_str = "Case #%d: %d"%(i+1,answer_num)
            print(answer_str)
            out.write(answer_str+'\n')
