import sys

if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1])

for test in range(input()):
    print "Case #{}:".format(test+1),

    s, m = raw_input().split()

    n = int(m)

    p = map(lambda ch: ch == "+", s)

    counter = 0

    for i in xrange(len(p) - n + 1):
        if not p[i]:
            counter += 1
            p[i:i+n] = map(lambda x: not x, p[i:i+n])

    possible = reduce(lambda x, y: x and y, p[-n:])

    if possible:
        print counter
    else:
        print "IMPOSSIBLE"
