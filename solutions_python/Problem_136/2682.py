def solve(C, F, X):
    c = 0
    t = 0
    cr = 2
    while c < X:
        if c >= C:
            if (X - c) / cr > (X - c + C) / (cr + F):
                cr += F
                c -= C
            else:
                t += (X - c) / cr
                break
        else:
            next_c = min(C, X)
            t += (next_c - c) / cr
            c = next_c
    return t

T = int(raw_input())
for i in range(1, T + 1):
    C, F, X = map(float, raw_input().split())
    print "Case #%d: %.8f" % (i, solve(C, F, X))
