#!python3.3
# coding=utf-8

import time
import math

inp = "C-small-attempt0.in"
out = inp.split(".")[0] + ".out"

num = lambda: nums()[0]
nums = lambda: [int(word) for word in words()]
words = lambda: line().split()
lines = lambda n: [line() in range(n)]
line = lambda: inpFile.readline().rstrip()
write = lambda s, *args: outFile.write(s.format(*args))


def main():
    global inpFile, outFile
    with open(inp) as inpFile:
        with open(out, "w") as outFile:
            start = time.time()

            T = num()
            for x in range(1, T + 1):
                solveC(x)

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


def solveC(x):
    i = ord('i')
    j = ord('j')
    k = ord('k')

    dict = {1: {1: +1, i: +i, j: +j, k: +k},
            i: {1: +i, i: -1, j: +k, k: -j},
            j: {1: +j, i: -k, j: -1, k: +i},
            k: {1: +k, i: +j, j: -i, k: -1}}

    _, X = nums()
    s = line()
    sLen = len(s)
    totalLen = sLen * X

    def lastMulIndex(start, target):
        mul = 1
        for index in range(start, totalLen):
            c = ord(s[index % sLen])
            mul = -dict[-mul][c] if mul < 0 else dict[mul][c]
            if mul == target:
                return index
        return None

    index = lastMulIndex(0, i)
    if index is not None:
        index = lastMulIndex(index + 1, j)
        if index is not None:
            index = lastMulIndex(index + 1, k)
            while index is not None and index < totalLen - 1:
                index = lastMulIndex(index + 1, 1)

    answer = "YES" if index is not None else "NO"
    write("Case #{}: {}\n", x, answer)


def solveD(x):
    X, R, C = nums()
    winner = "RICHARD" if (R * C) % X != 0 or R <= X - 2 or C <= X - 2 else "GABRIEL"
    write("Case #{}: {}\n", x, winner)


main()
