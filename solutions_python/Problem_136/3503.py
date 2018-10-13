import sys


def main():
    fin = open(sys.argv[1])
    eps = 0.0000001
    T = int(fin.readline())
    for test in range(1, T + 1):
        [C, F, X] = map(float, fin.readline().split())
        t = X / 2.0
        (f, newF) = (2, 2 + F)
        XmC = X - C
        while (X / newF - XmC / f) < eps:
            t = t - XmC / f + X / newF
            (f, newF) = (newF, newF + F)

        print "Case #%d: %.7f" % (test, t)


if __name__ == "__main__":
    main()
