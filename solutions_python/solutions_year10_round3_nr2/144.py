
import math

def solve(L,P,C):
    if L*C>=P:
        return 0
    t1 = L*math.sqrt(float(P)/L)
    fl = math.floor(t1)
    cl = math.floor(t1)
    if fl == L or cl == P:
        return 1 
    if math.floor(t1)==t1:
        return 1+solve(t1,P,C)
    else: 
        s1 = max(solve(L,math.floor(t1),C),solve(math.floor(t1),P,C))
        s2 = max(solve(L,math.ceil(t1),C),solve(math.ceil(t1),P,C))
        return 1+min(s1,s2)
        

T=int(input())
for case in range(1,T+1):
    L,P,C = [int(w) for w in input().split()]
    print("Case #{0}: {1}".format(case, solve(L,P,C)))
