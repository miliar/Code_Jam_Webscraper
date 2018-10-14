n = int(raw_input())
for i in xrange(n):
    s, k = raw_input().split()
    k = int(k)
    ans = 0
    while len(s) >= k:
        if s[0] == '-':
            ans += 1
            s = "".join("-+"[x == '-'] for x in s[1:k]) + s[k:]
        else:
            s = s[1:]

    if s.count("-") > 0:
        print "Case #{0}: IMPOSSIBLE".format(i + 1)
    else:
        print "Case #{0}: {1}".format(i + 1, ans)
