#!/usr/bin/env python2

import logging
from itertools import product

logging.basicConfig(filename='debug.log',level=logging.DEBUG)
log = logging.getLogger("default")

def is_valid(r, c, grid):
    empty, min_r, min_c, max_r, max_c = get_locations(r, c, grid)
    letters = min_r.keys()
    for letter in letters:
        min_r_letter = min_r[letter] - 1
        min_c_letter = min_c[letter] - 1
        max_r_letter = max_r[letter] - 1
        max_c_letter = max_c[letter] - 1

        for i in xrange(min_r_letter, max_r_letter + 1):
            for j in xrange(min_c_letter, max_c_letter + 1):
                if grid[i][j] != letter:
                    return False

    return True


def get_locations(r, c, grid):
    min_r = {}
    min_c = {}
    max_r = {}
    max_c = {}

    empty = []

    for i in range(r):
        row = grid[i]
        for j, letter in enumerate(row):
            if letter == '?':
                empty.append((i, j))
                continue

            min_r_letter = min_r.get(letter)
            if not min_r_letter:
                min_r[letter] = i + 1

            elif min_r_letter > i + 1:
                min_r[letter] = i + 1

            min_c_letter = min_c.get(letter)
            if not min_c_letter:
                min_c[letter] = j + 1

            elif min_c_letter > j + 1:
                min_c[letter] = j + 1

            max_r_letter = max_r.get(letter)
            if not max_r_letter:
                max_r[letter] = i + 1

            elif max_r_letter < i + 1:
                max_r[letter] = i + 1

            max_c_letter = max_c.get(letter)
            if not max_c_letter:
                max_c[letter] = j + 1

            elif max_c_letter < j + 1:
                max_c[letter] = j + 1

    return (empty, min_r, min_c, max_r, max_c)


def distribute(r, c, grid):
    (empty, min_r, min_c, max_r, max_c) = get_locations(r, c, grid)

    letters = list(min_r.keys())
    num_letters = len(letters)
    num_empty = len(empty)

    for choice in product(letters, repeat=num_empty):
        for index, loc in enumerate(empty):
            i, j = loc[0], loc[1]
            grid[i][j] = choice[index]

        if is_valid(r, c, grid):
            return grid

    return None


def print_grid(grid):
    for row in grid:
        print "".join(row)

n = int(raw_input())  # cases
log.debug("Test cases: %d" % n)

for i in xrange(1, n + 1):
    log.debug("Starting test case: %d" % i)
    r, c = [int(s) for s in raw_input().split(" ")]

    grid = []
    for j in xrange(1, r + 1):
        row_string = raw_input()
        row = list(row_string)
        grid.append(row)

    grid = distribute(r, c, grid)

    log.debug("Input: %d %d, output: %s" % (r, c, grid))

    print("Case #{}:".format(i))
    print_grid(grid)
