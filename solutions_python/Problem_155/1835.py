#!/usr/bin/env python
# Karl WNW
# input stdin, output stdout

"""
Input example:

4
4 11111
1 09
5 110011
0 1
"""

import sys


def solve(i):
    max_shyness, audience = map(str, sys.stdin.readline().split())
    max_shyness = int(max_shyness)

    num_friends_needed = 0
    counter_people = 0

    for shyness, num_people in enumerate(audience):
        num_people = int(num_people)

        if num_people and counter_people + num_friends_needed < shyness:
            num_friends_needed += shyness - counter_people - num_friends_needed

        counter_people += num_people
        if counter_people >= max_shyness:
            break

    print "Case #%d: %s" % (i, num_friends_needed)


def main():
    num_testcases = int(sys.stdin.readline().strip())
    for t in range(num_testcases):
        solve(t + 1)

if __name__ == '__main__':
    main()
