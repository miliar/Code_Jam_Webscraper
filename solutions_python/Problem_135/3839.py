#!/usr/bin/env python
import sys


next_line = lambda f: f.readline().strip()


def main(args):
    finp = args[1]
    finp = open(finp, "r")
    count = int(finp.readline())

    for testcase in range(count):
        row = int(next_line(finp))
        rows = [next_line(finp).split() for x in range(4)]
        s1 = {x for x in rows[row - 1]}

        row = int(next_line(finp))
        rows = [next_line(finp).split() for x in range(4)]
        s2 = {x for x in rows[row - 1]}

        intersection = s1 & s2
        if len(intersection) == 1:
            print("Case #%d: %s" % (testcase + 1, intersection.pop()))
        elif len(intersection) > 1:
            print("Case #%d: Bad magician!" % (testcase + 1))
        else:
            print("Case #%d: Volunteer cheated!" % (testcase + 1))

    return False


if __name__ == "__main__":
    sys.exit(main(sys.argv))