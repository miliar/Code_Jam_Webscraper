t = int(raw_input().strip())
for c in xrange(t):
    r1 = int(raw_input().strip())
    for i in xrange(4):
        if i == r1 - 1:
            s1 = set(map(int, raw_input().strip().split()))
        else:
            raw_input()

    r2 = int(raw_input().strip())
    for i in xrange(4):
        if i == r2 - 1:
            s2 = set(map(int, raw_input().strip().split()))
        else:
            raw_input()
    s = s1 & s2
    print "Case #%d:" % (c + 1),
    if len(s) == 0:
        print "Volunteer cheated!"
    elif len(s) == 1:
        print list(s)[0]
    else:
        print "Bad magician!"
