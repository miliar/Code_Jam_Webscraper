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
        testcase = InputCase()

        # Adjust test case variables here
        casestring = args.filename.readline()
        testcase.X, testcase.R, testcase.C = map(int, casestring.split())
        testcases.append(testcase)

    args.filename.close()

    return testcases

def puzzle(t):
    #print("%d %d %d" % (t.X, t.R, t.C))
    if (t.R * t.C) / t.X != (float(t.R) * t.C) / t.X: # if R*C doesn't divide evenly by X
        return "RICHARD"

    if t.X >= 3 and (t.R == 1 or t.C == 1):
        return "RICHARD"

    if t.X > (t.R * t.C):
        return "RICHARD"

    if t.X == 4 and (t.R == 2 or t.C == 2):
        return "RICHARD"

    return "GABRIEL"


def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for t in range(len(testcases)):
        print "Case #" + str(t + 1) + ": " + str(puzzle(testcases[t]))

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
