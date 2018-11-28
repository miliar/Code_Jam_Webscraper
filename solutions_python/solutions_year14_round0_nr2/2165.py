#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main():
    n = int(raw_input())
    for i in range(n):
        C, F, X = [float(s) for s in raw_input().split()]
        #~ print C, F, X
        curx = 0
        curs = 2.0
        sumt = 0
        while 1:
            t1 = (X-curx)/curs
            t2 = (X-(curx-C))/(curs+F)
            #~ print '[%0.3f]curx=%0.3f, curs=%0.3f, t1=%0.3f, t2=%0.3f'%(sumt,curx,curs,t1, t2)
            if(curx>=X):
                print 'Case #%d: %0.7f'%(i+1, sumt)
                #~ print '!'
                #~ print 
                break
            if(t1<=t2 or curx<C):
                # no need to buy, finished??
                minc = min(C, X-curx)
                sumt += minc/curs
                curx += minc
                #~ print 'NO BUY'
            else:
                # buy a farm
                #sumt += t2
                curs += F
                curx -= C
                #~ print 'BUY'
    return 0

if __name__ == '__main__':
    main()

