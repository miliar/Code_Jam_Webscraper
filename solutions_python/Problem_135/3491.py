import sys


def read_int(fp=sys.stdin):
    return int(fp.readline().strip())


def read_ints(fp=sys.stdin):
    return map(int, fp.readline().strip().split())


def solve():
    first_answer = read_int()
    first_rows = [read_ints() for _ in range(4)]
    possible = set(first_rows[first_answer - 1])

    second_answer = read_int()
    second_rows = [read_ints() for _ in range(4)]
    possible = possible.intersection(second_rows[second_answer - 1])

    if not possible:
        return "Volunteer cheated!"
    elif len(possible) == 1:
        return possible.pop()
    else:
        return "Bad magician!"

if __name__ == "__main__":
    T = read_int()
    for t in range(1, T+1):
        print "Case #%d: %s" % (t, solve())
