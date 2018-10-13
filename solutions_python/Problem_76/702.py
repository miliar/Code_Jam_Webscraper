from itertools import product, compress

def xum(L):
    S = L[0]
    for x in L[1:]:
        S^=x
    return S

def solvecase(L):
    l = len(L)
    counts = list(product([True, False],repeat=l))
    cl = 2**l
    divisions = []
    for i in range(1,cl//2):
        if xum(list(compress(L,counts[i])))==xum(list(compress(L,counts[cl-1-i]))):
            divisions.append(sum(list(compress(L,counts[i]))))
            divisions.append(sum(list(compress(L,counts[cl-1-i]))))
    return max(divisions) if len(divisions)>0 else 0

N = int(input())

for n in range(N):
    x = int(input())
    r = solvecase(list(map(int,input().split(' '))))
    if r==0: r = "NO"
    print("Case #"+str(n+1)+": "+str(r))
