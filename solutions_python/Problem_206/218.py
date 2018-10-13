import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    rr = []
    tt = I()
    for ti in range(1,tt+1):
        d,n = LI()
        rt = 1/inf
        for _ in range(n):
            i,k = LI()
            rt = max(rt, (d-i) / k)

        rr.append('Case #{}: {}'.format(ti, d/rt))

    return '\n'.join(rr)

print(main())
