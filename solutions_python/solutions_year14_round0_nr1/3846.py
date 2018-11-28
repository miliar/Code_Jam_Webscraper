"""When parsing game field, create two binary representations,
one for X (every X or T is 1, all else is 0),
and one for O. Also mark the fact that empty cells '.' are present.
"""
import sys


def read_case():
    choice = read_int()
    rows = [read_ints() for _ in xrange(4)]
    return choice, rows


def read_int():
    return int(sys.stdin.readline().strip())


def read_ints():
    line = sys.stdin.readline().strip()
    return map(int, line.split())


def main():
    n = read_int()
    for i in xrange(1, n + 1):
        choice1, rows1 = read_case()
        choice2, rows2 = read_case()

        common = tuple(frozenset(rows1[choice1 - 1]) & frozenset(rows2[choice2 - 1]))
        # print(choice1, rows1)
        # print(choice2, rows2)
        # print(common)

        if len(common) == 0:
            outcome = "Volunteer cheated!"
        elif len(common) == 1:
            outcome = str(common[0])
        elif len(common) > 1:
            outcome = "Bad magician!"
        else:
            raise ValueError

        sys.stdout.write("Case #{0}: {1}\n".format(i, outcome))

if __name__ == '__main__':
    main()
