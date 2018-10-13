from math import pi
from solver import solver


def small(ac, aj):
    if len(ac) < 2 and len(aj) < 2:
        return 2
    if len(ac) == 2 and len(aj) == 0:
        a, b = ac[0]
        c, d = ac[1]
    if len(ac) == 0 and len(aj) == 2:
        a, b = aj[0]
        c, d = aj[1]
    if d - a <= 720 or c - b >= 720:
        return 2
    return 4


@solver(lines_per_case="int(args[0])+int(args[1])")
def parents(lines):
    lc, lj = map(int, lines[0].split())
    ac = sorted(tuple(map(int, line.split()))
                for line in lines[1:1+lc])
    aj = sorted(tuple(map(int, line.split()))
                for line in lines[1+lc:])
    assert len(ac) == lc
    assert len(aj) == lj
    return small(ac, aj)

if __name__ == "__main__":
    parents.from_cli()
