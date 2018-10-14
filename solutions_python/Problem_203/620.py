import sys

def ri():
    return map(int, sys.stdin.readline().split())


T = int(input())


def fillinit(i,j):
    global r
    global c
    global a
    global aa
    global v
    B = i
    U = i
    L = j
    R = j
    for rr in range(i+1, r):
        if aa[rr][j] == '?':
            B = rr
        else:
            break
    for rr in range(i-1, -1, -1):
        if aa[rr][j] == '?':
            U = rr
        else:
            break
    for cc in range(j+1, c):
        if aa[i][cc] == '?':
            R = cc
        else:
            break
    for cc in range(j-1, -1, -1):
        if aa[i][cc] == '?':
            L = cc
        else:
            break
    #print(U, B, L, R)
    for rr in range(U, B+1):
        for cc in range(L, R+1):
            if aa[rr][cc] != '?':
                if rr != i and cc != j:
                    if rr < i:
                        if rr+1 > U:
                            U = rr+1
                    else:
                        if rr-1 < B:
                            B = rr-1
    #print(U, B, L, R)
    for rr in range(U, B+1):
        for cc in range(L, R+1):
            if aa[rr][cc] != '?':
                if rr != i and cc != j:
                    if cc > j:
                        if cc-1 < R:
                            R = cc-1
                    else:
                        if cc+1 > L:
                            L = cc+1
    #print(U, B, L, R)
    for rr in range(U, B+1):
        for cc in range(L, R+1):
            aa[rr][cc] = a[i][j]

for i in range(T):
    count = 0
    r, c = ri()
    a = [[] for j in range(r)]
    aa = [[] for j in range(r)]
    v = [[0 for jj in range(c)] for j in range(r)]
    for ii in range(r):
        a[ii] = list(input())

    for ii in range(r):
        aa[ii] =  a[ii][:]
    #print(a)

    for ii in range(r):
        for jj in range(c):
            if a[ii][jj] != '?':
                fillinit(ii,jj)

    #for rr in range(r):
    #    print(*a[rr])


    print("Case #%d:"%(i+1))
    for rr in range(r):
        print("".join(aa[rr]))
