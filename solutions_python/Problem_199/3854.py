__author__ = 'giagulei'

import sys


def parse_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        tests = f.readlines()
        counter = 1
        for l in tests:
            testcase = l.split()
            pancakes = testcase[0]
            K = int(testcase[1])
            # start processing
            result = 0
            for i in range(0, len(pancakes)):
                if (i + K) > len(pancakes):
                    break
                if pancakes[i] == '-':
                    pancakes = flip(pancakes, i, K)
                    result += 1
            for c in pancakes[-K:]:
                if c == '-':
                    result = 'IMPOSSIBLE'
                    break
            print 'Case #{}: {}'.format(counter, result)
            counter += 1
        f.close()


def flip(pancakes, start, k):
    newpanc = pancakes[0:start]
    for c in pancakes[start:start + k]:
        if c == '-':
            newpanc += '+'
        else:
            newpanc += '-'
    newpanc += pancakes[start+k:]
    return newpanc

parse_input(sys.argv[1])
