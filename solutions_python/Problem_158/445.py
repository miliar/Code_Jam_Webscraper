#!python3.3
# coding=utf-8

import time
import math

inp = "D-small-attempt0.in"
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
                solveD(x)

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
    def minMoveCount(P):
        P.sort()
        max = P.pop()
        moveCount = max

        if max > 3:
            for i in range(2, int(max / 2) + 1):
                P.append(i)
                P.append(max - i)

                countIfSplit = minMoveCount(P) + 1
                if moveCount > countIfSplit:
                    moveCount = countIfSplit

                P.remove(i)
                P.remove(max - i)

        P.append(max)
        return moveCount

    _ = num()
    P = nums()
    write("Case #{}: {}\n", x, minMoveCount(P))


def solveD(x):
    X, R, C = nums()
    winner = "RICHARD" if (R * C) % X != 0 or R <= X - 2 or C <= X - 2 else "GABRIEL"
    write("Case #{}: {}\n", x, winner)


main()
