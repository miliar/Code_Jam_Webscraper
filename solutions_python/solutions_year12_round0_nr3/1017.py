import sys

def ans(n, a):
    print 'Case #%d:'%n,
    print a

def cycles(x):
    e = [x,]
    for i in range(len(x)-1):
        x = x[-1]+x[:-1]
        e.append(x)
    return e

def are_recicled(a,b):
    x = "%d"%a
    y = "%d"%b
    return y in cycles(x)

def solve(A,B):
    x=0
    for n in range(A,B+1):
        for m in range(n+1,B+1):
            if are_recicled(n,m):
                x+=1
    return x

f = sys.stdin
n = int(f.readline())
for i in range(n):
    l = map(int, f.readline().split())
    A = l[0]
    B = l[1]
    ans(i+1, solve(A,B))
