__author__ = 'Vasilis Akoinoglou'

import numpy as np


__author__ = 'vasilisakoinoglou'

DEVEL = False

inputf = open('s_in.txt', 'r') if DEVEL else open('in.txt', 'r')

outputf = open('s_out.txt', 'w') if DEVEL else open('out.txt', 'w')

T = int(inputf.readline())

cases = []

lines = inputf.readlines(-1)


def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

cases = list(chunks(lines, 10))

print '=' * 80
print cases

def solve():
    results = []
    for i, case in enumerate(cases):
        casen = i + 1
        firstAnswer = int(case[0].strip())
        a = case[1:5][firstAnswer-1].strip().split(' ')
        secondAnswer = int(case[5].strip())
        b = case[6:10][secondAnswer-1].strip().split(' ')
        s = [set(a), set(b)]
        f = set.intersection(*s)
        common = list(f)
        x = ''
        if len(common) == 1:
            x = list(f)[0]
        elif len(common) == 0:
            x = 'Volunteer cheated!'
        elif len(common) > 1:
            x = 'Bad magician!'
        xs = "Case #%i: %s\n" % (casen, x)
        results.append(xs)
    outputf.writelines(results)

solve()