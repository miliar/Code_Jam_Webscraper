import sys


def time_to_next_farm(CPS, C):
    return C / CPS


def time_to_win(CPS, X):
    return X / CPS


def solve(C, F, X):
    T = 0.0
    CPS = 2.0
    play = True

    while play:
        ttnf = time_to_next_farm(CPS, C)
        ttwanf = time_to_win(CPS + F, X)
        ttw = time_to_win(CPS, X)

        if T + ttnf + ttwanf < T + ttw:
            T += ttnf
            CPS += F
        else:
            play = False

    return T + ttw


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            C, F, X = [float(v) for v in f.readline().strip().split()]
            result = solve(C, F, X)
            print "Case #%d: %.7f" % (t+1, result)


if __name__ == "__main__":
    main(sys.argv[1])
