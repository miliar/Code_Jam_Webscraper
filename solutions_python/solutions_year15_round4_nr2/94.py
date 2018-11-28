#!/usr/bin/python2.7


f = open('input.txt', 'r')
T = int(f.readline())

def solve(V, X, R_arr, C_arr):
    if len(R_arr) == 0:
        return -1
    elif len(R_arr) == 1:
        if C_arr[0] == X:
            return V / R_arr[0]
        else:
            return -1

    r1 = R_arr[0]
    r2 = R_arr[1]
    c1 = C_arr[0]
    c2 = C_arr[1]

    if c1 == X and c2 == X:
        return V / (r1 + r2)
    elif c1 != X and c2 != X:
        if (c1 - X) * (c2 - X) > 0:
            return -1
        else:
            dc1 = abs(c1 - X)
            dc2 = abs(c2 - X)
            v1 = dc2 / (dc1 + dc2) * V
            v2 = V - v1
            return max(v1 / r1, v2 / r2)
    else:
        if c1 == X:
            return V / r1
        else:
            return V / r2

for t in range(T):
    N, V, X = f.readline().rstrip().split(' ')
    N = int(N)
    V = float(V)
    X = float(X)
    R_arr = []
    C_arr = []
    for n in range(N):
        ri, ci = map(float, f.readline().rstrip().split(' '))
        R_arr.append(ri)
        C_arr.append(ci)

    print "Case #" + str(t + 1) + ":",
    time = solve(V, X, R_arr, C_arr)
    if time == -1:
        print 'IMPOSSIBLE'
    else:
        print time

