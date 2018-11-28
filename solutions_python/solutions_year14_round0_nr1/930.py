#! /usr/bin/python

def solve(answer1, grid1, answer2, grid2):
    options = frozenset(grid1[answer1 - 1]) & frozenset(grid2[answer2 - 1])
    if len(options) == 1:
        return iter(options).next()
    if not options:
        return 'Volunteer cheated!'
    return 'Bad magician!'


def main():
    t = input()
    for i in xrange(1, t + 1):
        answer1 = input()
        grid1 = read_grid()
        answer2 = input()
        grid2 = read_grid()
        print 'Case #{0}: {1}'.format(i, solve(answer1, grid1, answer2, grid2))


def read_grid():
    return [map(int, raw_input().split()) for i in xrange(4)]


if __name__ == '__main__':
    main()
