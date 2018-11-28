# crop.py

import sys
from itertools import islice

def main(inputfile):
    f = open(inputfile)
    ncases = int(f.next())
    for i,line in enumerate(f):
        print 'Case #%d: %d' % (i+1, solve(*map(int, line.strip().split())))

def solve(n, A, B, C, D, x0, y0, M):
    def coords():
        X,Y = x0,y0
        yield X, Y
        for i in range(1,n):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            yield X, Y
    trees = sorted(coords())
    assert len(trees) == n
    N = 0
    for i,(x1,y1) in enumerate(trees):
        for j,(x2,y2) in islice(enumerate(trees), i+1, n):
            for k,(x3,y3) in islice(enumerate(trees), j+1, n):
                (xc,xr),(yc,yr) = divmod(x1+x2+x3, 3), divmod(y1+y2+y3, 3)
                if xr or yr:
                    continue
                N += 1
    return N #+ len(trees)
        

if __name__ =='__main__':
    f = sys.argv[1] if len(sys.argv)>1 else 'A-sample.in'
    main(f)
