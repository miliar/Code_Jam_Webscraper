from math import sqrt, pow, log, ceil, log10
from sys import stdin, setrecursionlimit
import random

T = int(stdin.readline())
setrecursionlimit(1500)

def answer2(lis):

    C, F, X, prod, currenttime, currentmin = lis
 
    isFinished = False

    while isFinished == False:
        newcurrentmin = min(currentmin, X/prod + currenttime)

        if currenttime >= currentmin:
            isFinished = True

        if C / prod + currenttime >= currentmin:
            isFinished = True

        C, F, X, prod, currenttime, currentmin = [C, F, X, prod + F, C / prod + currenttime, newcurrentmin]

    return currentmin

for i in range(1,T+1):

    C, F, X = map(float, stdin.readline().split())
    
    print "Case #" + str(i) + ":", 

    ans = answer2([C, F, X, 2., 0, X/2.])

    print round(ans, 7)
