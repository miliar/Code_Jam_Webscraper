def fun(b, pan):
    M = len(b)
    c = 0
    for i, v in enumerate(b):
        if sum(b) == 0:
            return c

        if v:
            if i + pan  > M:
                return "IMPOSSIBLE"
            for j in xrange(pan):
                b[i+j] = not b[i+j]
            c += 1

t = int(raw_input())
for i in xrange(1, t + 1):
    pancakes, panSize = raw_input().split(" ")
    count = 0
    bp = [];
    for c in reversed(pancakes):
        bp.append(c == "-")

    print "Case #%s: %s" % (i, fun(bp, int(panSize)))