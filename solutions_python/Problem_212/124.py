
def solve(N, P, G):
    if P == 2:
        r0 = sum(1 for x in G if x % 2 == 0)
        r1 = N - r0
        return r0 + (r1 + 1) / 2
    if P == 3:
        r0 = sum(1 for x in G if x % 3 == 0)
        r1 = sum(1 for x in G if x % 3 == 1)
        r2 = N - (r0 + r1)
        if r1 > r2:
            rx = r2 + (r1 - r2 + 2) / 3
        else:
            rx = r1 + (r2 - r1 + 2) / 3
        return r0 + rx
    if P == 4:
        r0 = sum(1 for x in G if x % 3 == 0)
        r1 = sum(1 for x in G if x % 3 == 1)
        r2 = sum(1 for x in G if x % 3 == 2)
        r3 = N - (r0 + r1 + r2)
        r_even = r2 / 2
        r_odd = min(r1, r3)
        r1, r2, r3 = r1 - r_odd, r2 % 2, r3 - r_odd
        rx, rt = max(r1, r3), 0
        if rx >= 2 and r2:
            rx, r2, rt = rx - 2, 0, 1
        rt += rx / 4
        rt += 1 if rx % 4 else 0
        return r0 + r_even + r_odd + rt
        

T = int(raw_input())
for t in xrange(T):
    N, P = map(int, raw_input().split(' '))
    G = map(int, raw_input().split(' '))
    res = solve(N, P, G)
    print 'Case #%d: %s' % (t + 1, res)
