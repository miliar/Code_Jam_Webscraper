t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    s, k = raw_input().split(" ")
    k = int(k)
    a = [False if x == '-' else True for x in s]
    count = 0
    for j in range(len(s) - k + 1):
        if not a[j]:
            count += 1
            for l in range(k):
                a[j + l] = not a[j + l]

    ok = True
    for j in xrange(1, k+1):
        if not a[-j]:
            ok = False
            break

    if ok:
        print "Case #{}: {}".format(i, count)
    else:
        print "Case #{}: {}".format(i, 'IMPOSSIBLE')
