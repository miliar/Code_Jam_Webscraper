T = int(raw_input())
for t in range(1, T+1):
    a1 = int(raw_input())
    l1 = set([raw_input() for _ in range(4)][a1-1].split())
    a2 = int(raw_input())
    l2 = set([raw_input() for _ in range(4)][a2-1].split())
    r = l1.intersection(l2)
    if len(r) == 0:
        r = "Volunteer cheated!"
    elif len(r) == 1:
        r = list(r)[0]
    else:
        r = "Bad magician!"
    print "Case #%s: %s" % (t, r)
