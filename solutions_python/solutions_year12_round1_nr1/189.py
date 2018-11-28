def solve(A, B, p):
    p.append(0)
    prob = 1
    best = 2 + B
    for i in range(0, A + 1):
        cost = ((A - i) + (B - i) + 1) + (1 - prob) * (B + 1)
        best = min(cost, best)
        prob *= p[i]
    return best

T = int(input ())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    p = list(map(float, input().split()))
    print("Case #%d: %s" % (i, solve(A, B, p)))

