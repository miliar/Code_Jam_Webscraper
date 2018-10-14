
cases = input()
for case in range(1, cases + 1):
    n, a = raw_input().strip().split()
    ans = 0
    tot = 0
    for i, c in enumerate(a):
        s = int(c)
        if i > tot:
            ans += i - tot
            tot = i
        tot += s
    print "Case #%d: %d" % (case, ans)


