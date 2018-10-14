from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random


def s(r, n):
#   return 2*r*(n+0) + 2*((n+0)*(n+1)/2)
#   return 2*r*n + 2*(n*(n+1)/2)
    return 2*r*n + n + 4*((n-1)*n/2)

T = int(stdin.readline())

for i in range(1,T+1):

    line1, = map(int, stdin.readline().split())
    
    array1 = {}

    for j in range(1,5):
        array1[j] = map(int, stdin.readline().split())

    line2, = map(int, stdin.readline().split())
    
    array2 = {}

    for j in range(1,5):
        array2[j] = map(int, stdin.readline().split())

    # Solve
    sol = [x for x in array1[line1] if x in array2[line2]]
    
    print "Case #" + str(i) + ":", 

    if len(sol) == 1:
        print sol[0]
    elif len(sol) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
