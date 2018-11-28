t = int(raw_input())

for _ in xrange(t):
    x, r, c = [int(i) for i in raw_input().split(" ")]
    if x == 1:
        print "Case #{}: GABRIEL".format(_ + 1)
    elif x == 2:
        if (r * c) % 2:
            print "Case #{}: RICHARD".format(_ + 1)
        else:
            print "Case #{}: GABRIEL".format(_ + 1)
    elif x == 3:
        if (r in (2, 4) and c == 3) or (c in (2, 4) and r == 3) or (c == 3 and r == 3):
            print "Case #{}: GABRIEL".format(_ + 1)
        else:
            print "Case #{}: RICHARD".format(_ + 1)
    elif x == 4:
        if (r * c) % 4:
            print "Case #{}: RICHARD".format(_ + 1)
        elif (r in (4, 3) and c == 4) or (c in (4, 3) and r == 4):
            print "Case #{}: GABRIEL".format(_ + 1)
        else:
            print "Case #{}: RICHARD".format(_ + 1)
    else:
        print "ERR"
