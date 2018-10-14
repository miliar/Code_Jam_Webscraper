import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def solve(R, Y, B, rs, ys, bs):
    assert R >= max(Y, B)
    if Y + B > R * 2 or Y + B < R:
        return 'IMPOSSIBLE'
    else:
        k = len(ys) + len(bs) - len(rs)
        for i in xrange(k):
            ys[i] = ys[i] + bs[i]
        bs = bs[k:]

        assert len(ys) + len(bs) == len(rs)

        ans = ''
        while rs:
            ans += rs.pop()
            if ys:
                ans += ys.pop()
            else:
                ans += bs.pop()
        return ans


for no_t in xrange(1, read_int() + 1):
    N, R, O, Y, G, B, V = read_ints()

    if V + Y == N:
        ans = 'VY' * (N / 2) if V == Y else 'IMPOSSIBLE'
    elif B + O == N:
        ans = 'BO' * (N / 2) if B == O else 'IMPOSSIBLE'
    elif R + G == N:
        ans = 'RG' * (N / 2) if R == G else 'IMPOSSIBLE'
    else:
        #print(Y, B, R)
        if V > 0:
            ys = ['YV' * V + 'Y']; Y -= (V + 1)
        else:
            ys = []
        if O > 0:
            bs = ['BO' * O + 'B']; B -= (O + 1)
        else:
            bs = []
        if G > 0:
            rs = ['RG' * G + 'R']; R -= (G + 1)
        else:
            rs = []
        #print(ys, bs, rs)

        if Y < 0 or B < 0 or R < 0:
            ans = 'IMPOSSIBLE'
        else:
            ys += ['Y'] * Y
            bs += ['B'] * B
            rs += ['R'] * R

            R, Y, B = len(rs), len(ys), len(bs)
            ans = 0
            
            if Y >= max(R, B):
                R, Y = Y, R
                rs, ys = ys, rs
            elif B >= max(R, Y):
                R, B = B, R
                rs, bs = bs, rs

            ans = solve(R, Y, B, rs, ys, bs)

    print 'Case #%d: %s' % (no_t, ans)
