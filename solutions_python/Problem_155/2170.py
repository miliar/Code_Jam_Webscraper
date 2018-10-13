#!/usr/bin/python

import sys


def read_case(f):
    l = f.readline().strip()
    parts = l.split(' ')
    smax = int(parts[0])
    levels = map(int, parts[1])
    if len(levels) != smax + 1:
        raise ValueError('Bad levels len: ' + str(parts))
    return levels


def solve(levels):
    standing = 0
    friends = 0
    for level, count in enumerate(levels):
        # print 'loop', level, count, standing, friends
        if standing < level and count > 0:
            friends_to_add = level - standing
            friends += friends_to_add
            standing += friends_to_add

        standing += count

    return friends


def main(filename):
    with open(filename) as f:
        for case_num in range(int(f.readline())):
            result = solve(read_case(f))
            print 'Case #{}: {}'.format(case_num + 1, result)

if __name__ == "__main__":
    main(sys.argv[1])
