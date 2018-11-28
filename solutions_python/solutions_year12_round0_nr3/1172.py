import sys

def fact(n):
    v=1
    for i in range(1,n+1):
        v = v*i
    return v

def binom(n):
    return fact(n)/(2*fact(n-2))

def solve(A,B):
    intA    = int(A)
    intB    = int(B)
    resul   = 0
    m       = {}
    for nint in range(intA,intB+1):
        n = str(nint)
        count = 0
        for i in range(len(n)):
            newnint = int(n[i:] + n[:i])
            if newnint >= intA and newnint <= intB:
                if not newnint in m:
                    m[newnint] = True
                    count = count + 1
        if count > 1:
            resul = resul + binom(count)
            #print nint, count, resul
    return resul

T = int(sys.stdin.readline())
for i in range(T):
    data = sys.stdin.readline().strip().split(" ")
    A = data[0]
    B = data[1]
    print "Case #%d: %d"%(i+1,solve(A,B))
