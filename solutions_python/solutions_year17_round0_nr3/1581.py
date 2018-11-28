from heapq import *

t = int(input())

def push(a,b):
    if (b > 0):
        heappush(a,(-b,b))

for i in range(t):
    n, k = map(int,input().strip().split(' '))

    if n == k:
        print("Case #{}: {} {}".format(i+1,0,0))
        continue
    
    q = []
    
    push(q,n)
    
    for j in range(2,k+1):
        x = heappop(q)[1]

        ceil_max = (x-1)//2
        floor_max = (x-1)//2
        if x % 2 == 0:
            ceil_max += 1

        push(q,ceil_max)
        push(q,floor_max)

    _max = (q[0][1]-1)//2
    if q[0][1] % 2 == 0:
        _max += 1

    _min = (q[0][1]-1)//2
        
    print("Case #{}: {} {}".format(i+1,_max,_min))
