#!/usr/bin/env python3

def solve(N, V, X, R, C):
    assert 1 <= len(R) <= 2
    if len(C) == 1:
        if C[0] == X:
            return "{:0.6f}".format(V / R[0])
        else:
            return "IMPOSSIBLE"
    if C[0] == C[1]:
        if C[0] == X:
            return "{:0.6f}".format(V / sum(R))
        else:
            return "IMPOSSIBLE"
    
    if C[0] > X and C[1] > X or C[0] < X and C[1] < X:
        return "IMPOSSIBLE"
    t0 = V*(X-C[1])/R[0]/(C[0]-C[1])
    t1 = V*(X-C[0])/R[1]/(C[1]-C[0])
    assert t0 >= 0
    assert t1 >= 0
    return "{:0.6f}".format(max(t0, t1))

tests = int(input())
for test in range(tests):
    Ns, Vs, Xs = input().split()
    N, V, X = int(Ns), float(Vs), float(Xs)
    R, C = [], []
    for i in range(N):
        Ri, Ci = map(float, input().split())
        R.append(Ri)
        C.append(Ci)
    result = solve(N, V, X, R, C)
    print("Case #{}: {}".format(1+test, result))
