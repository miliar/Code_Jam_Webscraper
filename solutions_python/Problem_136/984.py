#! /usr/bin/env python

#import math

#  +---+---+---+
#  | a | b | c |
#  +---+---+---+
#  0   1   2   3
# -3  -2  -1

if __name__ == "__main__":
    T = int( input() )
    
    for x in range(1,T+1):

        C, F, X = map(float,input().split())
        
        c = 0.0
        cs = 2.0
        y = 0.0
        while (c < X):
            b = C / cs #buy
            w = X / cs #wait
            if (w < (b + X / (cs + F))):
                y = y + w
                c = X
            else:
                y = y + b
                cs = cs + F
        
        print('Case #%i: %.7f' % (x,y))