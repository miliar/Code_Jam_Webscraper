#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def Calc(C, F, X, rate):
    # if (X - C) / rate < X / (rate + F):
        # # stop buy
        # return X / rate
    # else:
        # # keep buy farm
        # return C / rate + Calc(C, F, X, rate + F)
    r = 0
    while(True):
        if (X - C) / rate < X / (rate + F):
            r += X / rate
            break
        else:
            r += C / rate
            rate += F
    return r

def main():
    if len(sys.argv) < 2:
        return
    f = open(sys.argv[1])
    fout = open(sys.argv[1] + '.out', 'w')
    T = int(f.readline())
    
    
    for t in xrange(0, T):
        C, F, X = f.readline().replace('\n', '').split(' ')
        res = round(Calc(float(C), float(F), float(X), 2), 7)
        #
        
        print 'Case #%d: %.7f' % (t+1, res)
        fout.write('Case #%d: %.7f\n' % (t+1, res))
    
    fout.close()
    f.close()

if __name__ == '__main__':
    main()

    
    # 1500/10 = 150
    # 2000/14 = 142
    
    # 1500/14 = 107.14
    # 2000/18 = 111.11