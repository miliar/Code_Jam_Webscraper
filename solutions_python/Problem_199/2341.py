# coding=utf-8

import sys


def solve(s, k):
    cnt = 0
    s = list(s)
    n = len(s)
    for i in range(n - k + 1):
        if s[i] == "-":
            cnt += 1
            for j in range(k):
                if s[i + j] == "+":
                    s[i + j] = "-"
                else:
                    s[i + j] = "+"
    if s.count("+") == n:
        return cnt


def main(argv=None):
    if argv is None:
        argv = sys.argv
    infile = argv[1]
    outfile = argv[2]
    pin = open(infile, "r")
    pout = open(outfile, "w")
    n = int(pin.readline().strip())
    for i in range(n):
        s, k = pin.readline().strip().split(" ")
        k = int(k)
        res = solve(s, k)
        pout.write("Case #" + str(i + 1) + ": " + ("IMPOSSIBLE" if res is None else str(res)) + "\n")
    pin.close()
    pout.close()


if __name__ == "__main__":
    main()
