T = int(raw_input().strip())

for i in xrange(T):
    X, R, C = map(int, raw_input().strip().split(' '))
    if min(R, C) == 1:
        if max(R, C) == 1:
            if X == 1:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
        elif max(R, C) == 2:
            if X < 3:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
        elif max(R, C) == 3:
            if X == 1:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
        else:  # max(R, C) == 4
            if X < 3:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
    elif min(R, C) == 2:
        if max(R, C) == 2:
            if X < 3:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
        elif max(R, C) == 3:
            if X < 4:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
        else:  # max(R, C) == 4
            if X < 3:
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
    elif min(R, C) == 3:
        if max(R, C) == 3:
            if X in (1, 3):
                winner = "GABRIEL"
            else:
                winner = "RICHARD"
        else:  # max(R, C) == 4
            winner = "GABRIEL"
    else:  # min(R, C) == 4
        if X != 3:
            winner = "GABRIEL"
        else:
            winner = "RICHARD"

    print "Case #%s: %s" % (i + 1, winner)
