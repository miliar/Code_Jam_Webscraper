import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    t = I()
    r = []
    for i in range(1,t+1):
        s, ts = S().split()
        a = [True if c=='+' else False for c in s]
        ti = int(ts)
        l = len(s)
        tr = 0
        for j in range(l):
            if a[j]:
                continue
            if j+ti > l:
                tr = 'IMPOSSIBLE'
                break
            tr += 1
            for k in range(j,j+ti):
                a[k] = not a[k]

        r.append('Case #{}: {}'.format(i,tr))

    return '\n'.join(r)



print(main())
