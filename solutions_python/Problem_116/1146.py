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

xt=('X','T')
ot=('O','T')

def readtrial(f):
    board= [ [c for c in readtext(f)] for x in xrange(4) ]
    for nt in (xt,ot):
        for line in board:
            if all((c in nt) for c in line):
                return '%s won'%(nt[0])
        for i in xrange(4):
            if all((c in nt) for c in [board[n][i] for n in xrange(4)]):
                return '%s won'%(nt[0])
        if all((board[i][i] in nt) for i in xrange(4)):
                return '%s won'%(nt[0])
        if all((board[i][3-i] in nt) for i in xrange(4)):
                return '%s won'%(nt[0])
    for line in board:
        for c in line:
            if c=='.':
                return 'Game has not completed'
    return 'Draw'

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
        f.readline()
        answer_str = "Case #%d: %s"%(i+1,str(answer))
        print answer_str
