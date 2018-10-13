#!/usr/bin/env python

"""
Python template for Google Code Jam problems
"""

import sys
import argparse

class InputCase: # Calling this "TestCase" will make PyCharm think it's a Python unittest
    pass

def process_command_line(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=argparse.FileType('r'),
                        help="Input file")
    args = parser.parse_args()

    return args

def process_input(args):
    casescount = int(args.filename.readline())
    testcases = []

    for i in range(casescount):
        casestring = args.filename.readline()

        testcase = InputCase()
        # Adjust test case variables here
        testcase.A, testcase.B, testcase.K = map(int, casestring.split())
        testcases.append(testcase)

    args.filename.close()

    return testcases

def puzzle(t):
    matches = 0
    for i in range(t.A):
        for j in range(t.B):
            if i & j < t.K:
                matches += 1

    return matches

def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for t in range(len(testcases)):
        print "Case #" + str(t + 1) + ": " + str(puzzle(testcases[t]))

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
