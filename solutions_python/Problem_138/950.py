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

        n = int ( input() )
        N = list(map(float,input().split()))
        K = list(map(float,input().split()))

        N.sort()
        #print(N)
        K.sort() #K.sort(reverse=True)
        #print(K)
        
        y = 0 #deceitful war
        z = 0 #war
        
        i = 0
        j = 0
        while (i < n):
            if (N[i] > K[j]):
                y = y + 1
                j = j + 1
            i = i + 1
        
        i = 0
        j = 0
        while (j < n):
            if (K[j] > N[i]):
                z = z + 1
                i = i + 1
            j = j + 1

        print('Case #%i: %i %i' % (x,y,n-z))
