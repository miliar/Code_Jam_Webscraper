import sys
import math

def main():
    #infile = open('in')
    #infile = open('B-large.in')
    infile = open('B-small-attempt0.in')
    #infile = open('B-small-practice.in')
    #infile = open('B-large-practice.in')
    outfile = open('out', 'w')
    T = long(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile.readline()) + '\n')

def solve(content):
    a,b,k = map(int, content.split())
    res = 0
    for i in range(a):
        for j in range(b):
            if (i & j) < k and i != j:
                res += 1
        if i < b and i < k:
            res += 1
    return str(res)

if __name__=='__main__':
    main()
