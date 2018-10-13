T = int(raw_input())

for case in xrange(T):
    ans = 0
    line = map(int, raw_input().split(' '))
    N, S, p = line[:3]
    scores = line[3:]

    for score in scores:
        if p == 0:
            ans += 1
        elif S == 0:
            if score >= 3 * p - 2 and 3 * p - 2 > 0:
                ans += 1
        elif S > 0:
            if p == 1 and score >= 1:
                ans += 1
            elif score >= 3 * p - 2 and 3 * p - 2 > 0:
                ans += 1
            elif score >= 3 * p - 4 and 3 * p - 4 > 0:
                ans += 1
                S -= 1

    print "Case #%s: %s" %(case+1, ans)
