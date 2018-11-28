from math import pi
from solver import solver


def solve(ps, areas, k):
    for i, (r, h) in enumerate(ps, 1):
        s0 = pi * r**2 + 2 * pi * r * h
        subareas = sorted(areas[i:], reverse=True)
        if len(subareas) < k-1:
            break
        yield s0 + sum(subareas[:k-1])


@solver(lines_per_case="args[0]")
def syrup(lines):
    n, k = map(int, lines[0].split())
    ps = sorted(tuple(map(int, line.split()))
                for line in lines[1:])[::-1]
    areas = [2 * pi * r * h for r, h in ps]
    return max(solve(ps, areas, k))

if __name__ == "__main__":
    syrup.from_cli()
