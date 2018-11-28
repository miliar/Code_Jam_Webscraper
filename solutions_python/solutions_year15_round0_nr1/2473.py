#!/usr/bin/env python
__author__ = 'kevindrosendahl'

import sys


def main(args):
    if not isinstance(args, list) or len(args) < 1:
        print "solution.py requires filename"
        exit(1)

    with open(args[0]) as input_file:
        lines = list(input_file)

    num_test_cases = int(lines[0])
    lines = map(lambda l: l.split(' ')[1].split('\n')[0], lines[1:])

    with open("output.txt", "w") as output_file:
        output_file.writelines(generate_output(num_test_cases, lines))


def generate_output(num_test_cases, test_cases):
    output = []
    for index in xrange(num_test_cases):
         output.append("Case #%d: %d\n" % (index + 1, generate_test_case_output(index, test_cases[index])))

    return output


def generate_test_case_output(test_case_number, test_case):
    num_invited = 0
    num_standing = 0

    for index, num_ovationarians in enumerate(test_case):
        num_need_to_invite = max(index - num_standing, 0)
        num_invited += num_need_to_invite
        num_standing += num_need_to_invite + int(num_ovationarians)

    return num_invited

###############################################################################
# BOOTSTRAP
###############################################################################
if __name__ == '__main__':
    main(sys.argv[1:])