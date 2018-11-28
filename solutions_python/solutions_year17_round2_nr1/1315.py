import sys

t = int(input())
for i in range(1, t + 1):
    line = input().split(" ")
    dest = int(line[0])
    n = int(line[1])
    slowest = 0
    for horse in range(1, n + 1):
        start, speed = [int(s) for s in input().split(" ")]
        if dest - start > 0:
            mpk = (dest - start)/speed
            if slowest < mpk:
                slowest = mpk

    if slowest == dest:
        slowest = 1;
    AnnieSpeed = dest / slowest
    print("Case #{}: {:.6f}".format(i, AnnieSpeed))
