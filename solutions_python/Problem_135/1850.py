import sys


def read_line():
    line = sys.stdin.readline()
    return [int(i) for i in line.strip().split()]


def get_options():
    row = int(sys.stdin.readline().strip())
    for i in xrange(4):
        if i + 1 == row:
            ret = read_line()
        else:
            read_line()

    return ret


def solve():
    options1 = set(get_options())
    options2 = set(get_options())

    common = options1.intersection(options2)

    if len(common) == 1:
        return list(common)[0]
    elif len(common) > 1:
        return 'Bad magician!'
    elif len(common) == 0:
        return 'Volunteer cheated!'


def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        print 'Case #{0}: {1}'.format(case + 1, solve())


if __name__ == '__main__':
    main()

