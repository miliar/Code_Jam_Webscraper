#! /usr/bin/python3
import sys
T = int(input())

for case_id in range(1, T + 1):
    X, R, C = map(int, input().split())

    winner = "GABRIEL"

    if ((R * C) % X or (X==4 and (R<=2 or C<=2))):
        winner = "RICHARD"
        X = 0

    print("Case #{0}: {1}".format(case_id, ":"), file=sys.stderr)
    for y in range(1, X // 2 + 2):
        x = X + 1 - y
        print(x,y, file=sys.stderr)
        if ((x > R and y > R) or (x > C and y > C)):
            winner = "RICHARD"
            break

    print("Case #{0}: {1}".format(case_id, winner))
