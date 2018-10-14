# coding: utf-8

from sets import *

if __name__ == '__main__':
    
    t = int(raw_input())
    
    for c in xrange(t):
        ans1 = int(raw_input())
        l1 = [map(int, raw_input().split()) for _ in xrange(4)][ans1-1]
        
        ans2 = int(raw_input())
        l2 = [map(int, raw_input().split()) for _ in xrange(4)][ans2-1]
        
        s = Set(l1).intersection(l2)
        
        if len(s) < 1:
            print 'Case #{}: Volunteer cheated!'.format(c+1)
        elif len(s) == 1:
            print 'Case #{}: {}'.format(c+1, s.pop())
        else: # len(s) > 1
            print 'Case #{}: Bad magician!'.format(c+1)
        
