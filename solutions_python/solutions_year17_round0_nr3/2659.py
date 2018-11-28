t = int(raw_input())
for c in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    stalls = [0, n + 1]
    for i in xrange(1, m + 1):
        l = len(stalls)
        j = 0
        point = 0
        max_dif = 0
        while j < l - 1:
            dif = stalls[j + 1] - stalls[j]
            if dif > max_dif:
                point = j
                max_dif = dif
            j += 1
            point2 = stalls[point] + max_dif / 2
        stalls.append(point2)
        stalls.sort()
    if max_dif % 2 == 0:
        print 'Case #%s: %d %d' % (c, point2 - stalls[point] - 1, stalls[point + 2] - point2 - 1)
    else:
        print 'Case #%s: %d %d' % (c, point2 - stalls[point], stalls[point + 2] - point2 - 2)
