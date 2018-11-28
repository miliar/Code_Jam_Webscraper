##import random
##
##import sys
##
##sys.setrecursionlimit(20000)

import math

def pair(n):
    if n % 2 == 1:
        return ((n-1)/2, (n-1)/2)
    else:
        return (n/2, n/2-1)

def prev_pair(x,y):
    if x == y:
        return (x,y-1)
    else:
        return (y,y)

def solve(n,k):
    if k == 1:
        return pair(n)
    else:
        a = int(math.log(k,2))
        b = int(math.log(n,2))
        k_res = k - 2**a
        n_res = n % 2**a
        x,y = pair(int(n/2**a))
        prev = prev_pair(x,y)
        if k_res <= n_res:
            return (x,y)
        else:
            return prev
        
        

f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):

    #read input
    n,k= [int(y) for y in f.readline().split('\n')[0].split(' ')]

    #solve
    ans1, ans2= solve(n,k)
    pr = "Case #"+str(i)+ ": " + str(ans1) + " " + str(ans2)
    #print pr
    g.write(pr + '\n')


f.close()
g.close()


