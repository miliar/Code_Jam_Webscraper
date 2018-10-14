#! /usr/bin/env python

#import math

#  +---+---+---+
#  | a | b | c |
#  +---+---+---+
#  0   1   2   3
# -3  -2  -1

#binary search
#        lo, hi = 1, t
#        while (lo <= hi):
#            k = (lo + hi) // 2
#            if k * (2*r + 2*k - 1) > t:
#                hi = k - 1
#            else:
#                lo, y = k + 1, k

def cons(s):
    return (s != 'a' and s != 'e' and s != 'i' and s != 'o' and s != 'u')    

if __name__ == "__main__":
    T = int( input() )
    
    for x in range(1,T+1):

        A, B = input().split()
        L = len(A)
        n = int(B)
        #print(A,L,n)
        
        y = 0
        
        for i in range(L):
            for j in range(i+n,L+1):
                s = A[i:j]
                for h in range(len(s)):
                    if len([k for k in s[h:h+n] if cons(k)]) >= n:
                        y = y + 1
                        break

        print('Case #%i: %i' % (x,y))
