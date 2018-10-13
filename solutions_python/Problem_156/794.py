import sys

def divhalf(a):
    c = a//2
    return c, a-c

def solve(P, d):
    mx = max(P)
    if mx == 0:
        return d
    elif mx == 1:
        return d+1
    P1 = P[:]
    i = P1.index(mx)
    a, b = divhalf(P1[i])
    P1[i] = a
    P1.append(b)
    P2 = [0 if p == 0 else p-1 for p in P]
    return min(solve(P2, d+1), solve(P1, d+1))

def solve(P):
    stack = []
    stack.append((P, 0))
    best = 10**10
    while stack:
        P_, d = stack.pop()
        if d > best:
            continue
        mx = max(P_)
        if mx <= 3 and d+mx < best:
            best = d+mx
            continue
        for c in range(1, mx//2+1):
            P__ = P_[:]
            i = P_.index(mx)
            P__[i] -= c
            P__.append(c)
            stack.append((P__, d+1))
        stack.append(([p-1 for p in P_], d+1))
    return best


if __name__ == '__main__':
    T = int(input())
    for case in range(1, T+1):
        D = int(input())
        P = [int(i) for i in input().split()]
        print("Case #%d: %s" % (case, solve(P)))
