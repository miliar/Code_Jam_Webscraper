t = int(raw_input())
for kei in xrange(1, t+1):
    s, k = raw_input().split(' ')
    k = int(k)
    s = [x == '+' for x in s]
    r = 0
    for i in xrange(len(s)-k+1):
        # print(s)
        if not s[i]:
            r += 1
            for j in xrange(i, i+k):
                s[j] = not s[j]
    print("Case #{}: {}".format(kei, r if all(s) else "IMPOSSIBLE"))
