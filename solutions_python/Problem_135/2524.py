#!/usr/bin/env python
out = open('test.out', 'w')
f = open('A-small-attempt0.in', 'r')
T = int(f.readline().strip())
for case in range(1, T+1):
    print case
    answer1 = int(f.readline())
    print answer1
    for i in range(4):
        row_cache = f.readline().split()
        if i + 1 == answer1:
            row1 = set(row_cache)
            print row1
    answer2 = int(f.readline())
    for i in range(4):
        row_cache = f.readline().split()
        if i + 1 == answer2:
            row2 = set(row_cache)
            print row2

    ans = row1 & row2
    if len(ans) == 1:
        for x in ans:
            out.write("Case #{}: {}\n".format(case, x))
    elif len(ans) == 0:
        out.write("Case #{}: Volunteer cheated!\n".format(case))
    elif len(ans) > 1:
        out.write("Case #{}: Bad magician!\n".format(case))
f.close()
out.close()
