t = int(raw_input())
for i in xrange(1, t + 1):
    dis, horse = [int(s) for s in raw_input().split(" ")]
    mintime = 0
    for j in xrange(horse):
        k, s = [int(s) for s in raw_input().split(" ")]
        k = dis - k
        s = float(s)
        if k/s > mintime: mintime = k/s
    print "Case #%d: %.6f" %(i,dis/mintime)
