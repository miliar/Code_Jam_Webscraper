#!/usr/bin/python3


def has_problem(R):
    for i in range(len(R)):
        if R[i] == R[i-1]:
            return True
    return False


def finished(C):
    for i,x in C:
        if x:
            return False
    return True

def step1(C):
    s = C[1][1] - C[2][1]
    R = [C[0][0], C[1][0]] * s
    C[0][1] -= s
    C[1][1] -= s
    return R

def step2(C):
    R = []
    while C[0][1] > min(C[1][1], C[2][1]):
        R.append(C[0][0])
        C[0][1] -= 1
        if C[1][1] >= C[2][1]:
            C[1][1] -= 1
            R.append(C[1][0])
        else:
            C[2][1] -= 1
            R.append(C[2][0])
    return R

def step3(C):
    s = max(0, C[0][1])
    R = [C[0][0], C[1][0], C[2][0]] * s
    C[0][1] -= s
    C[1][1] -= s
    C[2][1] -= s
    return R

def step4(C):
    s = max(0, C[1][1])
    R = [C[2][0], C[1][0]] * s
    C[1][1] -= s
    C[2][1] -= s
    return R

def step5(C):
    if not C[2][1]:
        return []
    C[2][1] -= 1
    return [C[2][0]]


T = int(input())


for t in range(T):
    
    N = "NROYGBV"
    X = [int(x) for x in input().split()]
    C = [[i, x] for i,x in enumerate(X) if N[i] not in "NOGV"]
    C.sort(key=lambda x: -x[1])
    
    R = []
    R.extend(step1(C))
    R.extend(step2(C))
    R.extend(step3(C))
    R.extend(step4(C))
    R.extend(step5(C))
    
    if finished(C):
        if X[0] != len(R) or has_problem(R):
            raise RuntimeError(X)
        print("Case #{0}: {1}".format(t+1, "".join([N[i] for i in R])))
    else:
        print("Case #{0}: IMPOSSIBLE".format(t+1))


