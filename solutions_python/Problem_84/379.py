import sys, math, re

def cover(f, y, x):
    f[y][x] = '/'
    if f[y][x+1]!='#':
        raise ValueError
    f[y][x+1] = '\\'
    if f[y+1][x]!='#':
        raise ValueError
    f[y+1][x] = '\\'
    if f[y+1][x+1]!='#':
        raise ValueError
    f[y+1][x+1] = '/'


def transform(f,r,c):
    #diagonal scan
    n = max(r,c)
    for i in xrange(n*n):
        for y in xrange(i,-1,-1):
            x = i - y
            if x>=c or y>=r:
                continue
            t = f[y][x]
            if t=='#':
                cover(f, y, x)

def main():
#    inFile = sys.__stdin__
#    outFile = sys.__stdout__
    inFile = open('A-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        r, c = map(int,inFile.readline().strip().split(' '))
        f = []
        for _ in xrange(r):
            f.append(list(inFile.readline().strip()))
            assert(len(f[-1])==c)
        outFile.write('Case #%d:\n' % t)
        try:
            transform(f,r,c)
            for row in f:
                outFile.write(''.join(row)+'\n')
        except:
            outFile.write('Impossible\n')

if __name__ == '__main__':
    main()
