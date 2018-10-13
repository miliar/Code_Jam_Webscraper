#!/usr/bin/python -tt

import sys

def parse_case(input_file):
    with open(input_file) as f:
        n_test_cases = int(f.readline())
        cases = []
        for case in xrange(n_test_cases):
            cases.append(map(int, f.readline().split()))
    return cases

def jam(case):
    n = case[0]
    s = case[1]
    p = case[2]
    winners = 0
    for i in xrange(n):
        total_score = case[i+3]
        if total_score % 3 == 1:
            if total_score / 3 + 1 >= p:
                winners += 1 
        elif total_score % 3 == 0:
            if total_score / 3 >= p:
                winners += 1
            elif s > 0 and total_score > 0 and total_score / 3 + 1 >= p:
                s -= 1
                winners += 1
        else:
            if total_score / 3 + 1 >= p:
                winners += 1
            elif s > 0 and total_score < 29 	and total_score / 3 + 2 >= p:
                s -= 1
                winners += 1
    return winners

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    cases = parse_case(sys.argv[1])
    i = 0
    for case in cases:
        i += 1
        print 'Case #%d: %d' % (i, jam(case))

if __name__ == '__main__':
    sys.exit(main())


