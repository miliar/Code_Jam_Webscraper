import sys
import time

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    D,N = readlist()
    mx = [readlist() for _ in range(N)] #Ki, Si
    ma = 0
    for k,s in mx:
        ma = max(ma, (D-k)/s)
    return D/ma

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
