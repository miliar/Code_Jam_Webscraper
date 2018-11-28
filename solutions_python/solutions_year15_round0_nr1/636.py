
def solve(t):
    _, S = raw_input().strip().split()

    ans = clapping = 0
    for s, n in enumerate(S):
        n = int(n)
        if clapping < s:
            ans += s - clapping
            clapping = s
        clapping += n

    print "Case #%d: %d" % (t, ans)


if __name__ == '__main__':
    T = int(raw_input().strip())
    for t in xrange(1, T+1):
        solve(t)
