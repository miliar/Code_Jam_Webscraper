#!/usr/bin/python2

T = int(raw_input().split()[0])

for case in range(T):
    [X, R, C] = map(int, raw_input().split())
    winnable = False    # Can Richard choose a piece that guarantees he wins

    # Dimensions
    if (R * C) % X != 0:
        winnable = True
    elif R == C and X > R * 2 - 1:
        winnable = True
    elif X > min(R, C) * 2:
        winnable = True
    else:
        # Now smaller than the field. Pockets?
        if X >= 7:
            winnable = True
        elif X == 4 and min(R, C) == 2:
            winnable = True

    if winnable:
        print 'Case #' + str(case + 1) + ': RICHARD'
    else:
        print 'Case #' + str(case + 1) + ': GABRIEL'
