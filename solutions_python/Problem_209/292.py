import sys
import time
import math

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    N,K = readlist()
    mx = [readlist() for _ in range(N)] #Ri, Hi
    mx2 = [(2*math.pi*r*h, r**2*math.pi) for r,h in mx]
    mx2.sort(key=lambda x:(-x[0],-x[1]))
    best = mx2[:K]
    rem = mx2[K:]
    best.sort(key=lambda x:(x[1],x[0]))
    bsurf = best[-1][1]
    best.sort(key=lambda x:(x[0],x[1]))
    rem.sort(key=lambda x:-(x[1]+x[0]))
    if len(rem)>0 and rem[0][0]+rem[0][1]-bsurf-best[0][0]>0:
        best[0] = rem[0]

    best.sort(key=lambda x:(-x[1],-x[0]))
    return best[0][1]+sum(v[0] for v in best)

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
