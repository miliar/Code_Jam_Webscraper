import re
import sys
import random
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())

sys.stdin = open('input.txt')
ofg=1
if ofg:
	sys.stdout = open('output.txt','w')

def follow(grid,w,h,direction,location):
    #print(grid,w,h,direction,location)
    location = [i+j for i,j in zip(direction,location)]
    while location[0] >=0 and location[0] < h and location[1] >=0 and location[1] < w:
        if(grid[location[0]][location[1]] != '.'):
            return 1
        location = [i+j for i,j in zip(direction,location)]
    return 0

dirt = {
    '^':(-1,0),
    'v':(+1,0),
    '<':(0,-1),
    '>':(0,+1),
}

for t in range(scan()):
    h,w = scan(),scan()
    grid = [scans() for i in range(h)]
    out = 0
    possible = 1
    for y in range(h):
        for x in range(w):
            if(grid[y][x]!='.'):
                if not follow(grid,w,h,dirt[grid[y][x]],[y,x]):
                    for i in dirt:
                        if follow(grid,w,h,dirt[i],[y,x]):
                            out+=1
                            break
                    else:
                        possible = 0
                        break
        else:
            continue
        break
    print('Case #%d:'%(t+1),('IMPOSSIBLE' if not possible else str(out)))
if ofg:
	sys.stdout.flush()
	sys.stdout.close()