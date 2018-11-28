T = int(raw_input())  

for K in xrange (T):
    s, k = [g for g in raw_input().split(" ")]
    k = int(k)
    l = len(s)

    cakes = []
    for c in s:
        if (c == '-'):
            cakes.append(False)
        elif (c == '+'):
            cakes.append(True)

    ans = 0;
    for i in xrange(l - k + 1):
        if (not cakes[i]):
            ans += 1
            for j in xrange(k):
                cakes[i + j] = not cakes[i + j]

    for i in xrange(l - k + 1, l):
        if (not cakes[i]):
            ans = -1
            break;

    if (ans >= 0):
        print "Case #{}: {}".format(K+1, ans)
    else:
        print "Case #{}: {}".format(K+1, 'IMPOSSIBLE')
