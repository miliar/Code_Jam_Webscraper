#!python3.3
# coding=utf-8

import time

inp = "A/A-large.in"
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
                solve(x)

            end = time.time()
            print("Solved in {:f} ms".format((end - start) / 1000))


def solve(x):
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


main()
