t = int(raw_input())
for i in xrange(1,t+1):
    n, l, h = map(int,raw_input().split())
    a = map(int,raw_input().split())
    possible = (h+1)*[True]
    for j in xrange(l):
        possible[j] = False
    for x in a:
        for j in xrange(1,h+1):
            if x%j != 0 and j%x != 0:
                possible[j] = False
    for j in xrange(l,h+1):
        if possible[j]:
            print "Case #%d: %d" % (i,j)
            break
    else:
        print "Case #%d: NO" % i
