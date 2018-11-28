from functools import  lru_cache

@lru_cache(maxsize=None)
def step(A,m):
    Arr = list(A)
    Arr.sort()
    Arr.reverse()
    if Arr[0]==0:
        return m
    
    r = 10000000
    
    for i in range(len(Arr)):
        Arr[i] = Arr[i]-1
    r = min(r,step(tuple(Arr),m+1))
    for i in range(len(Arr)):
        Arr[i] = Arr[i]+1    

    maxe = Arr[0]   

    if (maxe<2):
        return r
    
    for cut in range(2,maxe - 1):
        Arr[0]=maxe-cut
        Arr.append(cut)
        r = min(r,step(tuple(Arr),m+1))
        Arr = Arr[:-1]
        
    return r
    
t = int(input())
for i in range(t):
    n = int(input())
    A = [int(x) for x in input().split()]
    print("Case #{0}: {1}".format(i+1,step(tuple(A),0)))
