import sys
from math import ceil,floor

dd=0
#dd=1

if dd:
    def dprint(*x):
        print("".join([str(a) for a in x]))
else:
    def dprint(*x):
        1


def m():
    N=int(input())
    for n in range(N):
        print("Case #%d: "%(n+1),end="")
        solve(n)

def solve(i):
    n,k = map(int,input().strip().split())
    dprint("n=%d, k=%d"%(n,k))
    y,z = solver(n,k)
    print("%d %d"%(y,z))

def solver(n,k):
    if k==1:
        return ceil((n-1)/2),floor((n-1)/2)
    if n%2:
        return solver((n-1)//2,ceil((k-1)/2))
    if k%2:
        return solver(floor((n-1)/2),ceil((k-1)/2))
    return solver(ceil((n-1)/2),ceil((k-1)/2))

if __name__ == "__main__":
    m()



