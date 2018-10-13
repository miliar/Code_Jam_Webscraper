from __future__ import division
import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    t = 0.0
    R = 2.0
    [C, F, X] = [float(x) for x in sys.stdin.readline().strip().split()]
    
    while X/R > C/R+X/(R+F):
        t += C / R
        R += F
        
    t += X / R
            
    print 'Case #'+str(i+1)+': '+ "{:.7f}".format(t)
