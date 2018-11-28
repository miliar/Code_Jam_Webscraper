import sys
import numpy as np
import math


# TODO: ((2*X) > (R*C))
def solve(X, R, C):
    if (X >= 7) or X > (R*C) or ((R*C) % X != 0):
        return "RICHARD"
    # After this point: (R*C)%X == 0 -> True
    elif (X == 1) or (X == 2):
        return "GABRIEL"
    elif (R == 1) or (C == 1):
        return "RICHARD"
    elif (R < X) and (C < X):
        return "RICHARD"
    elif X == 3:
        return "GABRIEL"
    elif min(R, C) <= int(math.ceil(X/2.)):
        return "RICHARD"
    else:
        return "GABRIEL"

if __name__ == '__main__':
    f_in = open('D-small-attempt1.in', 'r')
    f_out = open('out_small.txt', 'w')
    cases = int(f_in.readline())
    for i in range(cases):
        [X, R, C] = map(int, f_in.readline().split())
        winner = solve(X, R, C)
        f_out.write('Case #' + str(i+1) + ": " + winner + "\n")