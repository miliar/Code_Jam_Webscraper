#!/usr/bin/python

import sys, operator

def getint():
    line = sys.stdin.readline().strip()
    return int(line)

cases = getint()
for case in range(1, cases + 1):
    combinations = {}
    oppositions = {}
    for c in 'QWERASDF': oppositions[c] = set()

    line = sys.stdin.readline().split()
    line.reverse()
    C = int(line.pop())
    for i in range(C):
        a0, a1, r = line.pop()
        combinations[(a0, a1)] = r
        combinations[(a1, a0)] = r
    D = int(line.pop())
    for i in range(D):
        a0, a1 = line.pop()
        oppositions[a0].add(a1)
        oppositions[a1].add(a0)

    stack = []
    opposition_stack = [set()]

    invocation = line[0]
    for c in invocation:
        if stack and (stack[-1], c) in combinations:
            stack.append(combinations[(stack[-1], c)])
            stack.pop(-2)
            opposition_stack.pop()
        elif c in opposition_stack[-1]:
            stack = []
            opposition_stack = [set()]
        else:
            stack.append(c)
            opposition_stack.append(opposition_stack[-1].union(oppositions[c]))
        #print c, stack, opposition_stack

    print 'Case #%d: [%s]' % (case, ', '.join(stack))

# vim:set ts=4 sw=4 et:
