#!/usr/bin/env python
import sys

def readboard(f):
    row1 = f.readline().strip().split()
    row2 = f.readline().strip().split()
    row3 = f.readline().strip().split()
    row4 = f.readline().strip().split()

    return [row1, row2, row3, row4]

with open(sys.argv[1]) as f:
    T = int(f.readline())

    for i in range(T):
        row1 = int(f.readline()) - 1
        board1 = readboard(f)
        r1 = set(board1[row1])

        row2 = int(f.readline()) - 1
        board2 = readboard(f)
        r2 = set(board2[row2])

        answers = r1 & r2

        if len(answers) == 1:
            s = str(answers.pop())
        elif len(answers) == 0:
            s = "Volunteer cheated!"
        else:
            s = "Bad magician!"

        print("Case #{}: {}".format(i+1, s))
