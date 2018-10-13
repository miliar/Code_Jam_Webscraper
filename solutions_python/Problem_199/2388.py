data = iter(open("A-large.in").read().splitlines())
T = int(next(data))
for caseNum in range(1, T + 1):
    ans = 0
    s, k = next(data).split()
    s, k = list(s), int(k)
    for i in range(len(s)-k+1):
        if s[i] != '+':
            ans += 1
            for j in xrange(i, min(len(s), i + k)):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
    ans = str(ans)
    if '-' in s:
        ans = "IMPOSSIBLE"

    print "Case #%d: %s" % (caseNum, ans)