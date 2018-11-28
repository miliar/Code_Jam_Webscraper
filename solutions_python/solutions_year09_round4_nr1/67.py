#!/usr/bin/python

import sys, os, re

def find_ith(i, lines):
    width = len(lines[0])
    n = 0
    for k in range(i, len(lines)):
        line = lines[k]
        ok = True
        #print line, i
        for j in range(i+1,width):
            #print "check", line[j]
            if line[j] == '1':
                ok = False
                break
        if ok:
            #print "OK,", line, i, n
            return n
        n += 1

def solve(f):
    n = int(f.readline())
    lines = []
    for i in range(0,n):
        lines.append(f.readline().strip())
    swapcnt = 0
    for i in range(0,n):
        ith = find_ith(i, lines)
        swapcnt += ith
        #print ith;
        #print "before", lines
        l = lines.pop(i + ith)
        lines.insert(i, l)
        #print "after", lines
    print swapcnt

def main():
    f = file(sys.argv[1])
    n = int(f.readline())
    for i in range(0, n):
        print "Case #%d:" % (i+1,),
        solve(f)

if __name__ == "__main__":
    main()
