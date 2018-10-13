#!/usr/bin/python3 -OO

import re


def get_needed_friend(shyness):
    level = 0
    friends = 0
    for (i, s) in enumerate(shyness):
        gap = max(i - level, 0)
        friends += gap
        level += gap
        level += s
    return friends


if __name__ == "__main__":
    with open("google_code_jam_input1.txt", 'r') as f:

        num_tests = int(f.readline())
        for i in range(1, num_tests + 1):
            test_line = re.match("(\d+) (\d+)", f.readline())
            num_shyness = int(test_line.group(1))
            shyness = map(int, list(test_line.group(2)))
            print("Case #%d: %d" % (i, get_needed_friend(shyness)))
