#!/usr/bin/env python

import sys, fractions, functools

# bot_to_string
def bts(b):
    if b == 'O': return 0
    if b == 'B': return 1

def stb(s):
    if s == 0: return 'O'
    if s == 1: return 'B'

def find_next_dest(v, i, bot):
    try:
        next = v.index(stb(bot),i+1)
        return int(v[next+1])
    except ValueError:
        return -1

def move(pos, dest):
    if pos < dest: return pos+1
    if pos > dest: return pos-1
    if pos == dest: return pos

def solve(N, v):
    dest = [0,0]
    i = 0
    cur = bts(v[i])
    dest[cur] = int(v[i+1])
    other = 1-cur
    dest[other] = find_next_dest(v,i+1,other)
    
    t = 0
    pos = [1,1]
    while(True):
        t = t + 1
        
        if(dest[other] != -1):
                pos[other] = move(pos[other], dest[other])
                
        if(pos[cur] == dest[cur]):
            # cur presses the button, prepare next step
            if (i + 2 >= len(v)):
                break
            i = i + 2
            cur = bts(v[i])
            dest[cur] = int(v[i+1])
            other = 1-cur
            dest[other] = find_next_dest(v,i+1,other)
            
        else:
            pos[cur] = move(pos[cur], dest[cur])
    
    return t
    

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    N = int(args[0])
    v = args[1:]
    result = solve(N,v)
    print("Case #%d: %d" % (case, result))
    case = case + 1
