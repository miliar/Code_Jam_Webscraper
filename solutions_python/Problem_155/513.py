T = int(raw_input())
for count in xrange(T):
    _, shies = raw_input().split()
    shies = map(int, shies)
    needed = 0
    standing = 0
    for i, shy in enumerate(shies):
        if standing < i:
            needed += 1
            standing += 1
        standing += shy
    print "Case #%d: %d" % (count + 1, needed)
