def solve(st, k):
    n = 0
    s = list(st)
    for i in xrange(0, len(s)- k + 1):
        if s[i] == '+':
            continue
        n = n + 1
        for j in xrange(0, k):
            if s[i+j] == '+':
                s[i+j] = '-'
            elif s[i+j] == '-':
                s[i+j] = '+'

    for i in xrange(len(s) - k, len(s)):
        if s[i] == '-':
            return "IMPOSSIBLE"
    return n

t = int(raw_input())
for i in xrange(1, t + 1):
    s, k = [x for x in raw_input().split(" ")]
    k = int(k)
    print "Case #{}: {}".format(i, solve(s, k))
