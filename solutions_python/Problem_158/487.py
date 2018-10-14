T = int(raw_input())
for _case_ in xrange(T):
    X, R, C = [int(_) for _ in raw_input().split()]
    winner = "RICHARD"
    if X == 1:
        winner = "GABRIEL"
    elif X == 2:
        if (R * C) % 2 == 0:
            winner = "GABRIEL"
    elif X == 3:
        if (R * C) % 3 == 0:
            if R * C > 3:
                winner = "GABRIEL"
    elif X == 4:
        if (R * C) % 4 == 0:
            if R * C >= 12:
                winner = "GABRIEL"
    print "Case #"+str(_case_+1)+": "+winner
