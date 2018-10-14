from decimal import Decimal
from operator import mul
import sys

with open(sys.argv[1]) as f:
    lines = int(f.readline().strip())
    for index in xrange(lines):
        A, B = map(int, f.readline().strip().split(' '))
        probs = map(float, f.readline().strip().split(' '))
        min = 2.0 + B
        for backspaces in xrange(0, A//2+1):
            correct = backspaces * 2.0 + B - A + 1.0
            incorrect = correct + B + 1.0
            correct_prob = reduce(mul, probs[:A-backspaces], 1.0)
            prob = correct_prob * correct + (1.0 - correct_prob) * incorrect
            if prob < min:
                min = prob
        print 'Case #%s: %.6f' % (index+1, Decimal(min))