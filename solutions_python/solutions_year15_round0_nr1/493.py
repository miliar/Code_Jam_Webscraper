T = int(raw_input())

for index in xrange(T):
    record = raw_input().split(' ')
    s_max = int(record[0])
    y = 0
    current = int(record[1][0])
    for i, k in enumerate(record[1][1:]):
     #   print i+1, y, current
        if int(k) != 0:
            y = y + max(0, i + 1 - current)
            current = max(i+1, current) + int(k)
    print "Case #%d: %d" % ((index+1), y)
