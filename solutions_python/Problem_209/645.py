def evaluate(P):
    if len(P) == 0:
        return 0

    PI = 3.14159265359 
    A = []

    A.append(P[0][0]*P[0][0] * PI)

    for p in P:
        A.append(p[0] * p[1] * 2 * PI)

    return sum(A)

def maximizeArea(A, P, k):
    if len(P) == 0 or len(A) == k:
        return A
    else:
        B = [x for x in A] + [P[-1]]
        C = [x for x in A]

        v1 = maximizeArea(B, P[0:-1], k)
        v2 = maximizeArea(C, P[0:-1], k)

        if evaluate(v1) > evaluate(v2):
            return v1
        else:
            return v2


T = int(raw_input(""))
for o in range(1, T+1):
    N, K = [int(x) for x in raw_input("").split(" ")]
    P = []
    for i in range(N):
        P.append([float(x) for x in raw_input("").split(" ")])

    P.sort()
    maxArea = maximizeArea([], P, K)

    print("case #%d: %f" % (o, evaluate(maxArea)))
