import sys
import heapq
import math

def printer(thigns):
    for i in thigns:
        sys.stdout.write(str(i))
    print("")

t = int(sys.stdin.readline())

sys.setrecursionlimit(100000)

gab = "GABRIEL"
ric = "RICHARD"

for j in range(t):
    linesplit = sys.stdin.readline().split()
    x = int(linesplit[0])
    r = int(linesplit[1])
    c = int(linesplit[2])

    totalArea = r*c;
    if totalArea%x != 0:
        printer(["Case #", j+ 1, ": ", ric])
        continue
    
    minSide = min(r,c)
    maxSide = max(r,c)
    if x <= minSide:
        printer(["Case #", j+ 1, ": ", gab])
        continue

    if x > maxSide:
        printer(["Case #", j+ 1, ": ", ric])
        continue

    if x >= 7:
        printer(["Case #", j+ 1, ": ", ric])
        continue

    if x <= (minSide - 1)*2:
        printer(["Case #", j+ 1, ": ", gab])
        continue

    if x > 1 + (minSide - 1)*2 and x > 2:
        printer(["Case #", j+ 1, ": ", ric])
        continue
    
    if minSide > 3:
        printer(["Case #", j+ 1, ": ", ric])
        continue


    if minSide == 3:
        if x == 6:
            printer(["Case #", j+ 1, ": ", ric])
            continue
        if x == 5:
            if maxSide > 6:
                printer(["Case #", j+ 1, ": ", gab])
            else:
                printer(["Case #", j+ 1, ": ", ric])
            continue
        else:
            printer(["Case #", j+ 1, ": ", gab])
            continue

    if minSide == 2:
        if x > 3:
            printer(["Case #", j+ 1, ": ", ric])
        else:
            printer(["Case #", j+ 1, ": ", gab])
        continue

    if minSide == 1:
        if x > 2:
            printer(["Case #", j+ 1, ": ", ric])
        else:
            printer(["Case #", j+ 1, ": ", gab])
        continue

    printer(["Case #", j+ 1, ": ", "error"])
    
