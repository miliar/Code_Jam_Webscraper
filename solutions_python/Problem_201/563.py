def divide(x):
    return (x/2, x/2) if x % 2 == 0 else (x/2 + 1, x/2)

def reccurSolve(y, z, a, b, K, t):
    if (1 << t) <= K < (1 << (t + 1)):
        procK = K - (1 << t) + 1
        if procK <= a: return divide(y - 1)
        else: return divide(z - 1)

    if y % 2 == 0:
        y, z = y/2, y/2 - 1
        a, b = a, a + 2*b
    else:
        y, z = y/2, y/2 - 1
        a, b, = 2*a + b, b

    return reccurSolve(y, z, a, b, K, t + 1)

def solve(N, K):
    return reccurSolve(N, 0, 1, 0, K, 0)

T = input()
for t in range(1, T + 1):
    N, K = map(int, raw_input().split())
    res = solve(N, K)
    print 'Case #%d: %d %d'%(t, res[0], res[1])
