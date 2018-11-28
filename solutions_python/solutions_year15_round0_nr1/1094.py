#!/usr/bin/env python

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
        testcase.smax = int(casestring.split()[0])
        testcase.s = casestring.split()[1]
        testcases.append(testcase)

    args.filename.close()

    return testcases

def puzzle(t):
    stringasints = [int(i) for i in t.s]

    acc = 0
    shortfall = 0
    for (i, s_i) in enumerate(stringasints):
        shortfall = max(shortfall, i-acc)
        acc += s_i

    return shortfall

def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for t in range(len(testcases)):
        print "Case #" + str(t + 1) + ": " + str(puzzle(testcases[t]))

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
