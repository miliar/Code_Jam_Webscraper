import sys


def input_reader(f):
    def _read_case():
        return [float(x) for x in fh.readline().split()]

    with open(f, "r") as fh:
        cases = int(fh.readline())
        for caseno in range(1,cases+1):
            yield caseno, _read_case()


def solve_case(C, F, X):
    """
    C -- farm cost in cookies
    F -- number of cookies a farm generates per second
    X -- goal number of cookies"""

    def _rate(farms):
        return 2 + farms * F

    def _delta(n):
        return (C-X)/_rate(n) + X/(_rate(n+1))

    t0 = float("inf")
    t = X/2
    n = 0
    while t < t0:
        t0 = t
        t = t0 + _delta(n)
        n += 1

    return t0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        infile = "/dev/stdin"
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        outfile = "/dev/stdout"
    with open(outfile, "w") as ofh:
        for caseno, case in input_reader(infile):
            print >> ofh, "Case #%d:" % caseno,
            print >> ofh, solve_case(*case)
