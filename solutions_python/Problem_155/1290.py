CA = input()

for tc in range(1, CA + 1):
    m, s = raw_input().split()
    have, extra = 0, 0
    m = int(m)
    for i, c in enumerate(s):
        if have < i:
            extra += i - have
            have = i
        have += int(c)




    print "Case #%d: %d" % (tc, extra)
