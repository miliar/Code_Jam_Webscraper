#!/usr/bin/env python
#By Jai Dhyani    

# usage: solution.py input_file
# prints solution to stdout
 
import sys
 
def solve( x ):
    return 0

def readints(f):
    return [int(x) for x in f.readline().split()]

def readtext(f):
    return f.readline()[:-1]

def readtrial(f):
    rows,columns=readints(f)
    lawn = [ readints(f) for x in xrange(rows) ]
    rmax = [ max(r) for r in lawn ]
    cmax = [ max([lawn[r][c] for r in xrange(rows)]) for c in xrange(columns) ]
    for r,row in enumerate(lawn):
        for c,h in enumerate(row):
            if h!=cmax[c] and h!=rmax[r]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename)
    try:
        numtrials = readints(f)[0]
    except IndexError as ie:
        print 'no input data in %s'%filename
        exit(0)
    for i in xrange(numtrials):
        answer = readtrial(f)
        answer_str = "Case #%d: %s"%(i+1,str(answer))
        print answer_str
