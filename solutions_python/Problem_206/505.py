# -*- coding: utf-8 -*-
import sys


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        n_cases = int(f.readline())
        for i in xrange(n_cases):
            D, N = map(int,f.readline().split())
            max_time = 0.
            for j in xrange(N):
                K,S = map(int,f.readline().split())
                t = float(D-K)/S
                if t > max_time:
                    max_time = t

            res = float(D)/max_time
            print 'Case #{}: {}'.format(i+1,res)
        
