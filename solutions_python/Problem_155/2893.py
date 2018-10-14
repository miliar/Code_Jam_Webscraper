T = int(raw_input())

for case in range(T):
    line = raw_input().split(' ')
    s_max = int(line[0])
    d = [int(i) for i in line[1]]
    d2 = [d[0]]
    for i in range(1, len(d)):
        d2.append(d2[i-1]+d[i])
    m = 0
    for i in range(1, len(d)):
        if (i-d2[i-1]) > m:
            m = i-d2[i-1]
    print "Case #%d: %d" % (case+1, m)
    