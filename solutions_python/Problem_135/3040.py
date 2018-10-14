import sys

T = int(sys.stdin.readline().strip())

for case_i in range(T):
    row_s1 = int(sys.stdin.readline().strip()) - 1
    arrange_1 = []
    for i in range(4):
        row = set(sys.stdin.readline().strip().split())
        arrange_1.append(row)

    row_s2 = int(sys.stdin.readline().strip()) - 1
    arrange_2 = []
    for i in range(4):
        row = set(sys.stdin.readline().strip().split())
        arrange_2.append(row)

    intersects = arrange_1[row_s1].intersection(arrange_2[row_s2])

    out = "Case #{0}: ".format(case_i + 1)
    if len(intersects) == 1:
        out += list(intersects)[0]
    elif len(intersects) > 1:
        out += "Bad magician!"
    else:
        out += "Volunteer cheated!"

    print out
