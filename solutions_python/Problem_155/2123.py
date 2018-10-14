__author__ = 'Joel Krebs'

import argparse
import sys


def aria(audience):
    friends = 0
    clapping = 0
    for shyness, people in enumerate(audience):
        friends_needed = max(shyness - clapping, 0)
        friends += friends_needed
        clapping += people
        clapping += friends_needed
    return friends


def main(input_file, outputfile):
    testcases = int(input_file.readline())
    for testcase in range(1, testcases + 1):
        audience = map(int, list(input_file.readline().split(' ')[1].rstrip('\n')))
        friends = aria(audience)
        outputfile.write("Case #{}: {}\n".format(testcase, friends))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin)

    parser.add_argument('outfile', nargs='?',
                        type=argparse.FileType('w'),
                        default=sys.stdin)

    opts = parser.parse_args()
    main(opts.infile, opts.outfile)