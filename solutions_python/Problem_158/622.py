T = int(raw_input())

for case in range(T):
    X, R, C = map(int, raw_input().split())
    winner = None
    if X == 1:
        assert winner is None or winner == "GABRIEL"
        winner = "GABRIEL"
    if (R * C) % X != 0:
        assert winner is None or winner == "RICHARD"
        winner = "RICHARD"
    if X > R and X > C:
        assert winner is None or winner == "RICHARD"
        winner = "RICHARD"
    if X == 2 and winner is None:
        winner = "GABRIEL"
    if (R == 1 or C == 1) and winner is None:
        winner = "RICHARD"
    if X == 3 and winner is None:
        winner = "GABRIEL"
    if (X, R, C) == (4, 2, 4):
        winner = "RICHARD"
    if (X, R, C) == (4, 3, 4):
        winner = "GABRIEL"
    if (X, R, C) == (4, 4, 2):
        winner = "RICHARD"
    if (X, R, C) == (4, 4, 3):
        winner = "GABRIEL"
    if (X, R, C) == (4, 4, 4):
        winner = "GABRIEL"
    print "Case #{}: {}".format(case + 1, winner)
