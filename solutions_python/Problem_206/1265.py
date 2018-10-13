def solve():
    D, N = map(int, raw_input().split())
    mxTime = None
    for _ in xrange(N):
        p, s = map(int, raw_input().split())
        myTime = ((D - p) * 1.0) / (s * 1.0)
        if mxTime is None or myTime > mxTime:
            mxTime = myTime
    return (D * 1.0) / mxTime


def main():
    tc = int(raw_input())
    for i in xrange(tc):
        ans = solve()
        print "Case #{}: {}".format(i + 1, ans)


if __name__ == '__main__':
    main()