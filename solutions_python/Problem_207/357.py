import sys
import time

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    N, R, O, Y, G, B, V = readlist()
    co = {'R':R, 'Y':Y, 'B':B}
    def getli():
        li = []
        if co['R']>0:
            li.append((co['R'],'R'))
        if co['Y']>0:
            li.append((co['Y'],'Y'))
        if co['B']>0:
            li.append((co['B'],'B'))
        li.sort()
        return li

    li = getli()
    first = li[0][1]
    res = first
    co[first]-=1
    while True:
        li = getli()
        if len(li) == 0:
            return res
        if res[-1] != first and co[first] > 0:
            res += first
            co[first]-=1
        elif res[-1] != li[-1][1]:
            res += li[-1][1]
            co[li[-1][1]]-=1
        elif len(li)>1 and res[-1] != li[-2][1]:
            res += li[-2][1]
            co[li[-2][1]]-=1
        else:
            return 'IMPOSSIBLE'
        

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
