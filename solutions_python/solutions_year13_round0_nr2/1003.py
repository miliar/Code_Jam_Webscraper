from __future__ import print_function
import sys
import itertools


def is_lawn_possible(lawn, m, n):
    rows, columns = get_upper_bounds(lawn, m, n)
    return all(
        lawn[i][j] >= rows[i] or lawn[i][j] >= columns[j]
        for i in range(m) for j in range(n)
    )


def get_upper_bounds(lawn, m, n):
    return [max(row) for row in lawn], \
        [max(lawn[i][j] for i in range(m)) for j in range(n)]


def read_lawns(path):
    with open(path) as f:
        lineiterator = iter(f)

        num_lawns = int(next(lineiterator))

        i = 0

        while i < num_lawns:
            dim = next(lineiterator).split()
            m, n = int(dim[0]), int(dim[1])

            yield [list(map(int, next(lineiterator).split())) for j in range(m)], m, n


def write_solutions(path, solutions):
    with open(path, "w") as f:
        for i, solution in zip(itertools.count(1), solutions):
            print("Case #{num}: {value}".format(num=i, value=solution), file=f)


if __name__ == '__main__':
    RESULTS = ["NO", "YES"]
    write_solutions(sys.argv[2], (RESULTS[is_lawn_possible(*lawn)] for lawn in read_lawns(sys.argv[1])))

