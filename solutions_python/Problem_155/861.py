#!/usr/bin/python
import fileinput


def get_cases():
    for line in fileinput.input():
        try:
            yield map(int, list(line.strip().split()[1]))
        except IndexError:
            pass


def solve(case):
    standing = 0
    friends_needed = 0
    for required, people_that_will_stand in enumerate(case):
        if people_that_will_stand > 0 and required > standing:
            extra_friends_needed = required - standing
            standing += extra_friends_needed
            friends_needed += extra_friends_needed
        standing += people_that_will_stand
    return friends_needed


if __name__ == '__main__':
    for num, case in enumerate(get_cases(), 1):
        solution = solve(case)
        print('Case #%d: %d' % (num, solution))
