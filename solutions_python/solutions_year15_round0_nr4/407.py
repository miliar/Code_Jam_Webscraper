from sys import stdin, stdout

RICHARD = "RICHARD"
GABRIEL = "GABRIEL"

T = int(stdin.readline().strip())

for case in range(1,T+1):
    X,R,C = map(int, stdin.readline().strip().split())
    if X == 1:
        winner = GABRIEL
    elif X == 2:
        if R * C % 2 != 0:
            winner = RICHARD
        else:
            winner = GABRIEL
    elif X == 3:
        if R * C % 3 != 0:
            winner = RICHARD
        else:
            if R * C > 3:
                winner = GABRIEL
            else:
                winner = RICHARD
    elif X == 4:
        if R * C % 4 != 0:
            winner = RICHARD
        else:
            if R * C == 12 or R * C == 16:
                winner = GABRIEL
            else:
                winner = RICHARD
    stdout.write("Case #{:d}: {:s}\n".format(case, winner))
