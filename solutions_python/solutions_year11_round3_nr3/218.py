#problem C

def valid(n,A):
    for a in A:
        if n%a!=0 and a%n!=0:
            return False
    return True

def makefactors(n,l,h):
    F = []
    for i in range(l,n//2+1):
        if n%i==0:
            F+=[i]
        if i>h:
            return set(F)
    return set(F)

def makemults(n,l,h):
    return set(range((l//n+1)*n, (h//n+1)*n,n))

T = int(input())

for t in range(T):
    N,L,H = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))

    R = makefactors(A[0],L,H) | makemults(A[0],L,H)
    for a in A:
        U = makefactors(a,L,H) | makemults(a,L,H)
        R &= U

    print("Case #"+str(t+1)+": "+(str(min(R)) if len(R)>0 else "NO"))
