t = int(raw_input())
for i in range(t):
    n, k = raw_input().split()
    s = int(n)

    count = 0
    num = 0

    for j in range(1, s + 1):
        num = num + int(k[j - 1])
        m = j - num
        if(m > 0):
            count = count + m
            num = num + m
    print "Case #%d: %d" % (i + 1, count)