#!/usr/bin/env python2.7
import sys

def print_output(case_no, answer):
    print "Case #{case_no}: {answer}".format(case_no=case_no, answer=answer)


def calc_invites(s_max, s_counts):
    invites = total =  0
    for i, x in enumerate(s_counts):
        if x and i > total:
            invites += i - total
            total += invites
        total += x

    return invites


def main(input):
    for case_no, line in enumerate(input):
        if case_no > 0:
            if len(line) > 2:
                s_max, sc = line.split()
                sc = [int(s) for s in sc]
                print_output(case_no, calc_invites(s_max, sc))
            else:
                print_output(case_no, 0)

if __name__ == '__main__':
    input = sys.argv[1]
    with open(input) as f:
        main(f)

