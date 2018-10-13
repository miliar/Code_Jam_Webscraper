import functools

def solve(N, K, U, P):
    while U > 0:
        min_P = min(P)
        argmins = [i for i in range(N) if P[i] == min_P]
        next_min_P = max(P)
        for i in range(N):
            if P[i] > min_P and P[i] < next_min_P:
                next_min_P = P[i]

        if next_min_P == min_P:
            return functools.reduce(lambda x, y: x*y, [min(p + U / N, 1.0) for p in P])
        elif (next_min_P - min_P) * len(argmins) > U:
            for i in argmins:
                P[i] += U / len(argmins)
            U = 0
        else:
            for i in argmins:
                P[i] += next_min_P - min_P
            U -= (next_min_P - min_P) * len(argmins)

    return functools.reduce(lambda x, y: x*y, P)

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
    U = float(input())
    P = [float(x) for x in input().split()]

    prob = solve(N, K, U, P)

    print("Case #%d: %.7f" % (t+1, prob))