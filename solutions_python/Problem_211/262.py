import sys
import time
import math

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    N,K = readlist()
    U = read(float)
    arr = readlist(float)
    arr.sort()
    while not(math.isclose(U,0)):
        cv = arr[0]
        cc = 1
        while len(arr)>cc and math.isclose(cv, arr[cc]):
            cc+=1
        nex = arr[cc] if len(arr)>cc else 1
        nex -= cv
        modif = min(U,nex*cc)
        U-=modif
        for i in range(cc):
            arr[i]+=modif/cc
        if modif < 0.00000001:
            break
    res = 1
    for p in arr:
        res *= p
    return res

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
