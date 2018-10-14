#!/usr/bin/env python
import sys

class coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class triangle:
    def __init__(self,c1,c2,c3):
        self.coords = [c1,c2,c3]

    def center(self):
        x_cent = 0
        y_cent = 0
        for c in self.coords:
            x_cent += c.x
            y_cent += c.y
        return coord(x_cent/3., y_cent/3.)
        
def comp_coord(n, A, B, C, D, x0, y0, M):
    comp_list = []
    X = x0
    Y = y0
    comp_list.append(coord(X, Y))
    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        comp_list.append(coord(X,Y))
    return comp_list

def comb(l,n):
    if n==0: yield []
    else:
        for i in xrange(len(l)):
            for cc in comb(l[i+1:],n-1):
                yield [l[i]]+cc

def do_it(all_c):
    #comb of coordinates
    all = [(a.x,a.y) for a in all_c]
    ok = 0
#    print all
#        print [(a.x,a.y) for a in c],(center.x,center.y)
    for c in comb(all_c,3):
        center = triangle(c[0],c[1],c[2]).center()
        if (center.x - int(center.x)) + (center.y - int(center.y)) == 0:
            ok += 1
    return ok
    
if __name__ == '__main__':
    #read input
    inp = open(sys.argv[1])
    out = open('crop.out','w')
    n_cases = int(inp.readline().strip())
    for i in range(n_cases):
        #parsing
        n, A, B, C, D, x0, y0, M = map(int, inp.readline().strip().split())
        c = comp_coord(n, A, B, C, D, x0, y0, M)
        print >>out, 'Case #%i: %i' % (i+1, do_it(c))
    out.close()
