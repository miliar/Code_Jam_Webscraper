#!/usr/bin/python3
import sys, re
readline = sys.stdin.readline

N = int(readline())
for case in range(1, 1 + N):
    L = int(readline())
    tree = ''.join(readline() for line in range(L))
    tree = ','.join(tree.split()).replace('(,', '(').replace('(', 'P(')
    tree = re.sub('([a-z]+)', r'"\1"', tree)

    print('Case #{0}:'.format(case))

    A = int(readline())
    for animal in range(A):
        features = set(readline().split()[2:])
        def P(weight, feature=None, if_true=1, if_false=1):
            if feature in features:
                return weight * if_true
            else:
                return weight * if_false
##        print(tree)
        prob = eval(tree, dict(P=P))
        print('{0:f}'.format(prob))
