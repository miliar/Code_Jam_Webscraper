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
    for ti in range(1,t+1):
        n = I()
        a = [int(c) for c in str(n)]
        l = len(a)
        if l == 1:
            tr = a[0]
        else:
            for _ in range(20):
                for i in range(l-1):
                    if a[i] > a[i+1]:
                        a[i] -= 1
                        for j in range(i+1,l):
                            a[j] = 9
                        break
            tr = int(''.join(map(str,a)))

        r.append('Case #{}: {}'.format(ti,tr))

    return '\n'.join(r)



print(main())
