T = int(raw_input())
for case in xrange(T):
    X, R, C = map(int, raw_input().split())
    if R > C:
        R, C = C, R
    # R is smaller dimension
    if (R * C) % X != 0:
        winner = "RICHARD"
    elif X >= 7:
        winner = "RICHARD"
    elif X > C:
        winner = "RICHARD"
    elif X >= 2 * R + 1:
        winner = "RICHARD"
    elif X % R == 0 and X >= R + 2:
        winner = "RICHARD"
    else:
        winner = "GABRIEL"

    print "Case #%d: %s" % (case + 1, winner)
