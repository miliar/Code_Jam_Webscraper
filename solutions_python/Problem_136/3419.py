# coding: utf-8

import sys

if __name__ == '__main__':
    
    t = int(raw_input())
    
    for case in xrange(t):
        c, f, x = map(float, raw_input().split())

        mintime = float(sys.maxint - 1)

        i = 0

        while True:
            
            if i * c > x:
                break
            
            tmp = x / (2 + i * f) + sum( (c / (2 + k * f) for k in xrange(i)) )
            
            mintime = min(mintime, tmp)
            
            i += 1

        print 'Case #{}: {}'.format(case+1, mintime)
