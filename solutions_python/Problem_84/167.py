# -*- coding: utf-8 -*-

import sys

def solve(tiles, v, h):
    for y in range(v-1):
        for x in range(h-1):
            if tiles[(x,y)] == tiles[(x+1,y)] == tiles[(x,y+1)] == tiles[(x+1,y+1)] == "#":
                tiles[(x,y)] = "/"
                tiles[(x+1,y)] = "\\"
                tiles[(x,y+1)] = "\\"
                tiles[(x+1,y+1)] = "/"
    
    for y in range(v):
        for x in range(h):
            if tiles[(x,y)] == "#":
                print "Impossible"
                return
    
    for y in range(v):
        print "".join([tiles[(x,y)] for x in range(h)])

def main():
    f = sys.stdin
    n = int(f.readline())
    for i in range(n):
        v,h = [int(s) for s in f.readline().split()]
        tiles = {}
        for y in range(v):
            line = f.readline()
            for x in range(h):
                tiles[(x,y)] = line[x]
        print "Case #%d:" % (i+1)
        solve(tiles, v, h)
    
main()
