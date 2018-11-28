# coding=utf-8

import sys


def solve(r, c, m):
    for i in range(r):
        s = None
        for j in range(c):
            if m[i][j] != "?":
                s = m[i][j]
                break
        if s is None:
            continue
        for j in range(c):
            if m[i][j] == "?":
                m[i][j] = s
            else:
                s = m[i][j]
    for j in range(c):
        s = None
        for i in range(r):
            if m[i][j] != "?":
                s = m[i][j]
                break
        for i in range(r):
            if m[i][j] == "?":
                m[i][j] = s
            else:
                s = m[i][j]
    return m


def main(argv=None):
    if argv is None:
        argv = sys.argv
    infile = argv[1]
    outfile = argv[2]
    pin = open(infile, "r")
    pout = open(outfile, "w")
    n = int(pin.readline().strip())
    for i in range(n):
        r, c = pin.readline().strip().split(" ")
        r = int(r)
        c = int(c)
        m = []
        for j in range(r):
            m.append(list(pin.readline().strip()))
        res = solve(r, c, m)
        pout.write("Case #" + str(i + 1) + ":\n")
        for j in range(r):
            pout.write("".join(res[j]) + "\n")

    pin.close()
    pout.close()


if __name__ == "__main__":
    main()
