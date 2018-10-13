import itertools
import sys


def calc_unhappiness(grid):
    walls = set()

    for x in grid:
        if (x[0] - 1, x[1]) in grid:
            walls.add(((x[0] - 1, x[1]), (x[0], x[1])))

        if (x[0] + 1, x[1]) in grid:
            walls.add(((x[0], x[1]), (x[0] + 1, x[1])))

        if (x[0], x[1] - 1) in grid:
            walls.add(((x[0], x[1] - 1), (x[0], x[1])))

        if (x[0], x[1] + 1) in grid:
            walls.add(((x[0], x[1]), (x[0], x[1] + 1)))

    return len(walls)

def solve_problem(r, c, num):
    if num == 0:
        return 0

    unhappy = sys.maxint

    for combo in itertools.combinations(itertools.product(range(r), range(c)), num):
        unhappy = min(unhappy, calc_unhappiness(combo))

    return unhappy


if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        r, c, num = map(int, sys.stdin.readline().split())

        print "Case #{0}: {1}".format(i, solve_problem(r, c, num))
