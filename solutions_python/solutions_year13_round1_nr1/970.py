import sys
import math

def main():
    #infile = open('A-large-practice-1.in')
    infile = open('A-small-attempt0.in')
    outfile = open('out', 'w')
    T = int(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile.readline()) + '\n')

def solve(content):
    r, t = map(long, content.split())
    def f(x):
        return (2*r+2*x-1)*x - t
    b = (2*r-1)
    d = b**2 + 8*t
    res = long(math.floor((-b + d**0.5)/4))
    if f(res) > 0 : res -= 1
    return str(res)

if __name__=='__main__':
    main()
