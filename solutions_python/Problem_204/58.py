def solve():
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = []
    for i in xrange(N):
        a = map(int, raw_input().split())
        a.sort()
        Q.append(a)
    ptr = [0 for i in xrange(N)]
    for i in xrange(N):
        ptr[i] = 0
        for j in xrange(P):
            if Q[i][j] * 100 < R[i] * 90:
                ptr[i] += 1
            else:
                break
    ans = 0
    lo = [None for i in xrange(52)]
    hi = [None for i in xrange(52)]
    while True:
        ok = False
        for i in xrange(N):
            if ptr[i] == P:
                ok = True
        if ok:
            break
        bound = 0
        min_hi = 10**9
        max_lo = -1
        for i in xrange(N):
            lo[i] = (100 * Q[i][ptr[i]] + 110 * R[i] - 1) // (110 * R[i])
            hi[i] = (100 * Q[i][ptr[i]]) // (90 * R[i])
            if hi[i] < hi[bound]:
                bound = i
            min_hi = min(min_hi, hi[i])
            max_lo = max(max_lo, lo[i])
        if min_hi == 0 or min_hi < max_lo:
            ptr[bound] += 1
        else:
            ans += 1
            for i in xrange(N):
                ptr[i] += 1
    return ans


def main():
    t = int(raw_input())
    for qq in xrange(t):
        ans = solve()
        print "Case #{0}: {1}".format(qq + 1, ans)

if __name__ == '__main__':
    main()
