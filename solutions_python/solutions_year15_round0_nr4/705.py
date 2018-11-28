def check_winner(X, R, C):
    MAX_MIN = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 3}
    if X == 1:
        return "GABRIEL"
    if X >= 7:
        return "RICHARD"
    if R*C % X != 0:
        return "RICHARD"
    if R < X and C < X:
        return "RICHARD"
    if min(R, C) < MAX_MIN[X]:
        return "RICHARD"
    return "GABRIEL"


T = input()

for casenbr in range(T):
    X, R, C = [int(n) for n in raw_input().split()]
    winner = check_winner(X, R, C)

    print "Case #%d: %s" % (casenbr+1, winner)
