def isTidy(x):
    l = map(int, str(x))
    return all(l[i] <= l[i + 1] for i in xrange(len(l) - 1))

t = int(raw_input())
for i in xrange(1, t + 1):
    _x = int(raw_input())

    while not isTidy(_x):
        _x -= 1

    print "Case #" + str(i) + ": " + str(_x)