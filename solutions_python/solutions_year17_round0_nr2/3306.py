#!/usr/bin/env python3

import math
import sys


def is_valid(value):
    last = "0"
    for c in value:
        if c < last:
            # print("  Valid failure: %s is not <= %s" % (c, last))
            return False
        last = c
    return True

def check(orig, answer):
    if not is_valid(str(answer)):
        print("  Answer %s for input %s is not valid" % (answer, orig))
        return False
    for i in range(answer + 1, orig + 1):
        if is_valid(str(i)):
            print("  Found higher valid value %s than %s for input %s" % (i, answer, orig))
            return False
    return True


def main():
    lines = sys.stdin.readlines()
    n = int(lines[0])
    for case, line in enumerate(lines[1:n+1]):
        value = [c for c in line.strip()]
        orig = list(value)
        for i in range(1, len(value)):
            if value[-i - 1] > value[-i]:
                pre = list(value)
                value[-i - 1] = chr(ord(value[-i - 1]) - 1)
                mid = list(value)
                for j in range(1, i + 1):
                    value[len(value) - j] = "9"
        while value[0] == "0":
            value = value[1:]
        # if int("".join(orig)) < 10 ** 8:
        #    assert int("".join(value)) <= int("".join(orig)), "%s %s" % (int("".join(value)), int("".join(orig)))
        #    assert check(int("".join(orig)), int("".join(value)))
        print("Case #%d: %s" % (case + 1, "".join(value)))


if __name__ == "__main__":
    main()
