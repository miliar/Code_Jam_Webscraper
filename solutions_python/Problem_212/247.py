# P = 2

# 1 1
# 2

# P = 3
# (1 2)
# (1 1 1)
# (2 2 2)
# (3)

# P = 4
# (1 1 1 1)
# (3 3 3 3)
# (2 1 1)
# (2 3 3)
# (1 3)
# (2 2)
# (4)


cases = int(raw_input())

for ctr in xrange(cases):
    ss = raw_input().split(" ")
    n = int(ss[0])
    p = int(ss[1])
    ss = raw_input().split(" ")
    groups = [int(s) for s in ss]

    answer = None
    if p == 2:
        g0 = [x for x in groups if x % 2 == 0]
        g1 = [x for x in groups if x % 2 == 1]
        answer = len(g0) + (len(g1) + 1) / 2
    elif p == 3:
        g0 = [x for x in groups if x % 3 == 0]
        g1 = [x for x in groups if x % 3 == 1]
        g2 = [x for x in groups if x % 3 == 2]
        answer = len(g0)
        while len(g1) > 0 and len(g2) > 0:
            answer += 1
            g1.pop()
            g2.pop()
        if len(g1) > 0:
            answer += (len(g1) + 2) / 3
        if len(g2) > 0:
            answer += (len(g2) + 2) / 3
    else:
        g0 = [x for x in groups if x % 4 == 0]
        g1 = [x for x in groups if x % 4 == 1]
        g2 = [x for x in groups if x % 4 == 2]
        g3 = [x for x in groups if x % 4 == 3]
        answer = len(g0)

        while len(g1) > 0 and len(g3) > 0:
            answer += 1
            g1.pop()
            g3.pop()

        while len(g2) > 1:
            answer += 1
            g2.pop()
            g2.pop()

        while len(g2) > 0 and len(g1) > 1:
            answer += 1
            g2.pop()
            g1.pop()
            g1.pop()

        while len(g2) > 0 and len(g3) > 1:
            answer += 1
            g2.pop()
            g3.pop()
            g3.pop()

        if len(g1 + g2 + g3) > 0:
            answer += 1

    print "Case #{}: {}".format(ctr + 1, answer)
