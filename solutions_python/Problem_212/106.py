import sys
from collections import defaultdict

def read_int():
    return int(sys.stdin.next())


def read_ints():
    return map(int, sys.stdin.next().split(' '))


def read_float():
    return float(sys.stdin.next())


def read_floats():
    return map(float, sys.stdin.next().split(' '))


def answer(P, sizes):
    residues = defaultdict(list)

    for size in sizes:
        residues[size % P].append(size)

    if P == 2:
        return len(residues[0]) + (len(residues[1])+1)/2
    if P == 3:
        zero, one, two = len(residues[0]), len(residues[1]), len(residues[2])
        common = min([one, two])

        return zero + common + (one + two - 2 * common + 2) / 3
    if P == 4:
        zero, one, two, three = len(residues[0]), len(residues[1]), len(residues[2]), len(residues[3])
        common = min([one, three])
        left_over = (one + three - 2 * common)
        extra_two = two % 2
        if extra_two == 0:
            return zero + two / 2 + common + (left_over + 3) / 4
        if extra_two == 1:
            return zero + two / 2 + common + (left_over + 2 + 3) / 4


if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        N, P = read_ints()
        sizes = read_ints()

        queries.append((P, sizes))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(answer(*q))])

