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
        
        _, S = input().split()
        
        standing = int(S[0])
        needed = 0
        
        # total = [0 for i in range(len(S))]
        # total[k] = standing
        
        for k in range(1,len(S)):
            
            ready = int(S[k])
            
            # print('k: %i\nstanding: %i\nready: %i\nneeded:%i\n' % (k,standing,ready,k-standing))
            
            if standing < k:
                needed += k - standing
                standing += ready + (k - standing)
            else:
                standing += ready
        
        print('Case #%i: %i' % (x,needed))
