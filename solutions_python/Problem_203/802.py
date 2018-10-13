import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

name = sys.argv[1]
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

def get_neigh(r, c, R, C, G):
    ret = []
    if r > 0:
        ret.append(G[(r-1, c)])
    if c > 0:
        ret.append(G[(r, c-1)])
    if r < R:
        ret.append(G[(r+1, c)])
    if c < C:
        ret.append(G[(r, c+1)])
    return ret

for testCase in range(1, T + 1):
    G = {}
    U, L = {}, {}
    D, R = {}, {}
    
    KIDS = set([])
    max_r, max_c = map(int, input().split())
    for r in range(max_r):
        A = input().strip()
        for c in range(max_c):
            G[(r,c)] = A[c]
            if A[c] != '?':
                U[A[c]] = r
                L[A[c]] = c
                D[A[c]] = r
                R[A[c]] = c
                KIDS.add(A[c]) 
    def try_l(k):
        if L[k] <= 0:
            return False
        for i in range(U[k], D[k]+1):
            if G[(i,L[k]-1)] != '?':
                return False
        for i in range(U[k], D[k]+1):
            G[(i,L[k]-1)] = k    
        L[k]-=1
        #eprint("try_l", k, L[k])
        return True

    def try_r(k):
        if R[k] >= max_c - 1: 
            return False
        for i in range(U[k], D[k]+1):
            if G[(i,R[k]+1)] != '?':
                return False
        for i in range(U[k], D[k]+1):
            G[(i,R[k]+1)] = k
        R[k]+=1
        #eprint("try_r", k, R[k])
        return True

    def try_u(k):
        if U[k] <= 0:
            return False
        for i in range(L[k], R[k]+1):
            if G[(U[k]-1, i)] != '?':
                return False
        for i in range(L[k], R[k]+1):
            G[(U[k]-1, i)] = k
        U[k]-=1
        return True

    def try_d(k):
        if D[k] >= max_r - 1:
            return False
        for i in range(L[k], R[k]+1):
            if G[(D[k]+1, i)] != '?':
                return False
        for i in range(L[k], R[k]+1):
            G[(D[k]+1, i)] = k
        D[k]+=1
        return True
    
    eprint("max", max_r, max_c)
    grow = True
    while (grow):
        grow = False
        for k in KIDS:
            if try_l(k) or try_r(k) or try_u(k) or try_d(k):
                #eprint("la", k, U[k], L[k], D[k], R[k])
                grow = True
        
    print("Case #" + str(testCase) + ":")    
    for r in range(max_r):
        for c in range(max_c):
            print(G[(r,c)], end='')
        print('')

