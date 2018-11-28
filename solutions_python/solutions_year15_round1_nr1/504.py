import sys
import math

def main():
    #infile = open('in')
    infile = open('A-large.in')
    #infile = open('A-small-attempt0.in')
    #infile = open('A-small-practice.in')
    #infile = open('A-large-practice.in')
    outfile = open('out', 'w')
    T = long(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile) + '\n')

def solve(infile):
    n = long(infile.readline())
    m = map(long, infile.readline().split())
    r1 = 0
    r2 = 0
    dx = 0
    c = m[0]
    for i in range(1, n):
        if m[i] < c:
            r1 += c - m[i]
            if c - m[i] > dx:
                dx = c - m[i]
        c = m[i]
    c = m[0]
    if dx > 0:
        for i in range(1, n):
            if c > dx:
                r2 += dx
            else:
                r2 += c
            c = m[i]
    else:
        r2 = 0
    return str(r1) + ' ' + str(r2)

if __name__=='__main__':
    main()
