__author__ = 'gingva'

import sys,operator,time



def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            t = time.time()
            ncases = int(f.next().strip())
            for n in range(ncases):
                L = int(f.next().strip('\r\n'))
                plates = [int(c) for c in f.next().strip('\r\n').split()]
                assert(len(plates) == L)
                a,b = solve(plates)
                print>>g, 'Case #%d: %d %d'  % (n+1, a,b )
                print 'Case #%d: %d %d'  % (n+1, a,b )


from pylab import *

def solve(plates):
    d = diff(plates)
    a = abs(sum(d[d<0]))

    r = abs(min(0,min(d)))
    d2 = maximum(-array(plates[0:-1]),-r*ones(shape(d)))
    b = abs(sum(d2[d2<0]))


    return a,b



if __name__ == '__main__':
    main('A-test.in', 'A-test.out')
    main('A-small-attempt0.in', 'A-small-attempt0.out')
    main('A-large.in', 'A-large.out')


