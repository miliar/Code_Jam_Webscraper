from multiprocessing import Pool

def solve((N, R, P, S)):
    for i in xrange(N):
        r = 0
        p = 0
        s = 0
        while R > 0 or P > 0 or S > 0:
            if R > 0 and P == 0 and S == 0:
                return 'IMPOSSIBLE'
            if R == 0 and P > 0 and S == 0:
                return 'IMPOSSIBLE'
            if R == 0 and P == 0 and S > 0:
                return 'IMPOSSIBLE'
            if min(R, P, S) == S and R > 0 and P > 0:
                p += 1
                R -= 1
                P -= 1
            if min(R, P, S) == R and P > 0 and S > 0:
                s += 1
                P -= 1
                S -= 1
            if min(R, P, S) == P and S > 0 and R > 0:
                r += 1
                S -= 1
                R -= 1
        R = r
        P = p
        S = s
    ans = ''
    if R > 0:
        ans = 'R'
    if P > 0:
        ans = 'P'
    if S > 0:
        ans = 'S'
    for i in xrange(N):
        s = ''
        for ch in ans:
            if ch == 'R':
                s += 'RS'
            if ch == 'S':
                s += 'PS'
            if ch == 'P':
                s += 'PR'
        ans = s
    l = list(ans)
    for i in xrange(N):
        x = 2 ** (N - i - 1)
        y = 2 ** i
        for j in xrange(x):
            i1 = 2 ** y * j
            i2 = i1 + y
            i3 = i2 + y
            if l[i1:i2] > l[i2:i3]:
                l[i1:i2], l[i2:i3] = l[i2:i3], l[i1:i2]
    return ''.join(l)

T = int(raw_input())
p = Pool(4)
args = []
for i in range(T):
    N, R, P, S = map(int, raw_input().split())
    args.append((N, R, P, S))
ans = p.map(solve, args)
for i in range(T):
    print 'Case #%d:' % (i + 1), ans[i]
