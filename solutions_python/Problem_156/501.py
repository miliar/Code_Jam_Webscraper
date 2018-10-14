#!python3.3
# coding=utf-8

import time
import math

inp = "B-small-attempt1.in"
out = inp.split(".")[0] + ".out"

num = lambda: nums()[0]
nums = lambda: [int(word) for word in words()]
words = lambda: line().split()
lines = lambda n: [line() in range(n)]
line = lambda: inpFile.readline()
write = lambda s, *args: outFile.write(s.format(*args))


def main():
    global inpFile, outFile
    with open(inp) as inpFile:
        with open(out, "w") as outFile:
            start = time.time()

            T = num()
            for x in range(1, T + 1):
                solveB(x)

            end = time.time()
            print("Solved in {:f} ms".format((end - start) / 1000))


def solveA(x):
    _, S = words()

    total = 0
    shyness = 0
    totalMissing = 0
    for count in (int(s) for s in list(S)):
        if shyness > total:
            missing = shyness - total
            totalMissing += missing
            total += missing
        total += count
        shyness += 1

    write("Case #{}: {}\n", x, totalMissing)


def solveB(x):
    _ = num()
    P = nums()
    write("Case #{}: {}\n", x, minMoveCount(P))


def minMoveCount(P):
    P.sort()
    max = P.pop()
    moveCount = max
    #selectedMovements = ["reduce by {}".format(max)]

    if max > 3:
        for i in range(2, int(max / 2) + 1):
            j = max - i
            #[countIfSplit, movements] = minMoveCount(P + [i, j])
            countIfSplit = minMoveCount(P + [i, j])
            if moveCount > countIfSplit + 1:
                moveCount = countIfSplit + 1
                #selectedMovements = ["split {} as {} + {}".format(max, i, j)] + movements

    #return [moveCount, selectedMovements]
    return moveCount


main()
