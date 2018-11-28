import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

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
    tt = I()
    rr = []
    for ti in range(1,tt+1):
        n,p = LI()
        g = LI()
        c = collections.defaultdict(int)
        for gi in g:
            c[gi%p] += 1
        r = c[0]
        if p == 2:
            r += (c[1] + 1) // 2
        elif p == 3:
            r += min(c[1],c[2])
            k = max(c[1],c[2]) - min(c[1],c[2])
            r += (k+2) // 3
        elif p == 4:
            r += (c[2] + 1) // 2
            r += min(c[1],c[3])
            k = max(c[1],c[3]) - min(c[1],c[3])
            if c[2] % 2 == 1:
                if k > 1:
                    r += 1
                    k -= 2
            r += (k+3) // 3

        rr.append('Case #{}: {}'.format(ti, r))

    return '\n'.join(rr)


print(main())
