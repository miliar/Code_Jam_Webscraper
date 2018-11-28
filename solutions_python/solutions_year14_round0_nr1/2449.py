#!/usr/bin/env python
import sys

def solve(first_ans, first_set, sec_ans, sec_set):
    new_set = [val for val in first_set[first_ans] if val in sec_set[sec_ans]]

    if len(new_set) == 1:
        return new_set[0]
    elif len(new_set) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"



if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        f = open(sys.argv[1])

    num_tests = int(f.readline())

    for x in xrange(num_tests):
        first_ans = int(f.readline()) - 1
        first_set = [f.readline().split() for i in xrange(4)]
        sec_ans = int(f.readline()) - 1
        sec_set = [f.readline().split() for i in xrange(4)]

        result = solve(first_ans, first_set, sec_ans, sec_set)
        print "Case #%d: %s" % (x+1, result)
