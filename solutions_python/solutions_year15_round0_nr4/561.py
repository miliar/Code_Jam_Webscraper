import math

T = int(raw_input())

for case in range(T):
    X, R, C = map(lambda x: int(x), raw_input().split())

    if X >= 7:
        solution = 0
    elif X == 1:
        solution = 1
    elif X > (R*C):
        solution = 0
    elif (R*C) >= X and (R*C) % X != 0:
        solution = 0
    elif X > R and X > C:
        solution = 0
    elif X == 2:
        solution = 1
    elif X == 3:
        solution = 0 if min(R, C) == 1 else 1
    else:
        D_med = int(math.ceil(X/2.0))

        if R == 1 or C == 1:
            solution = 0
        elif D_med > max(R, C):
            solution = 0
        elif D_med == min(R, C):
            solution = 0
        else:
            solution = 1

    print 'Case #%d: %s' % (case+1, 'GABRIEL' if solution == 1 else 'RICHARD')