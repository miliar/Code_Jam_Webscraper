import numpy as np
from collections import deque

def solve(s,k):
    if goal(s):
        return 0
    tabu = []
    q = deque([])
    q.appendleft((s,0))
    while len(q)>0:
        x = q.pop()
        if goal(x[0]):
            return x[1]       
        if x[0] in tabu:
            continue
        tabu.append(x[0])
        for i in range(len(x[0])-k+1):
            q.appendleft((flip(x[0],k,i),1+x[1]))
    return "IMPOSSIBLE"
           
def goal(s):
    return sum(s)==len(s)

def degree(s):
    deg = 0
    for i in range(len(s)-1):
        if s[i+1]!=s[i]:
            deg+=1
    return deg

def flip(s,k,i):
    s1 = list(s)
    for j in range(k):
        s1[i+j] = 1 - s1[i+j]
    return s1

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(T):
        s,k = raw_input().split(" ")
        k = int(k)
        s = [int(c=='+') for c in s]
        n = solve(s,k)
        print "Case #{}: {}".format(t+1,n)
