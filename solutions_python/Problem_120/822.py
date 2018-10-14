from math import *

def sol(r, t):
    a  = 2.0
    b = (2*r-1)
    c = -t
    return floor((-b + sqrt(b**2 - 4*a*c)) / (2*a))

T = int(input())

for i in range(1,T+1):
    r, t = [int(x) for x in input().split()]
    print("Case #" + str(i) + ": " + str (sol(r, t)))

    
