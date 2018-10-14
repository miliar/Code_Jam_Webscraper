# coding=utf-8

import sys


def ok(a, begin):
    i = begin
    while i < len(a) - 1:
        if a[i + 1] > a[i]:
            return True
        if a[i + 1] < a[i]:
            return False
        i += 1
    return True


def solve(k):
    a = list(str(k))
    b = [0] * len(a)
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(a)):
        if ok(a, i):
            b[i] = a[i]
        else:
            b[i] = a[i] - 1
            j = i + 1
            while j < len(a):
                b[j] = 9
                j += 1
            break
    res = 0
    for i in range(len(b)):
        res = res * 10 + b[i]
    return res


def main(argv=None):
    if argv is None:
        argv = sys.argv
    infile = argv[1]
    outfile = argv[2]
    pin = open(infile, "r")
    pout = open(outfile, "w")
    n = int(pin.readline().strip())
    for i in range(n):
        k = pin.readline().strip()
        k = int(k)
        res = solve(k)
        pout.write("Case #" + str(i + 1) + ": " + str(res) + "\n")
    pin.close()
    pout.close()


if __name__ == "__main__":
    main()
