__author__ = 'Alexander Leid'

import sys


def standing_ovation(data):
    total = 0
    friends = 0

    for i in range(len(data)):

        if i > total:
            friends += i - total
            total = i

        total += data[i]
    return friends


def main():
    lines = sys.stdin.readlines()
    lines = lines[1:]
    case = 0

    for line in lines:
        case += 1
        data = line.strip().split()[1]

        print 'Case #{0}: {1}'.format(case, standing_ovation(map(int, data)))


if __name__ == '__main__':
    main()
