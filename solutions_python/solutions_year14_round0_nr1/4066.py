#!/usr/bin/env python
#
# Google Code Jam '14
# jx2zhou
#
#####

t = int(input())

lines = []

for i in range(t):
    # Get first square
    r_1 = int(input())
    square_1 = [list(map(int, input().split()))
                for j in range(4)]
    row_1 = square_1[r_1 - 1]

    # Get second square
    r_2 = int(input())
    square_2 = [list(map(int, input().split()))
                for j in range(4)]
    row_2 = square_2[r_2 - 1]

    # Check for matches
    possibles = set(row_1).intersection(set(row_2))
    if len(possibles) == 0:
        lines.append("Volunteer cheated!")
    elif len(possibles) == 1:
        lines.append(str(possibles.pop()))
    else:
        lines.append("Bad magician!")

for i, line in enumerate(lines):
    print("Case #" + str(i + 1) + ": " + line)
