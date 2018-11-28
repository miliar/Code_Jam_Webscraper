import sys
import copy

__author__ = 'David'

sys.setrecursionlimit(5000)


def solve(stack, flipper_size):
    #print stack
    if len(stack) == 0:
        return 0
    if stack[0] == '+':
        return solve(stack[1:], flipper_size)
    if stack[0] == '-':
        if len(stack) >= flipper_size:
            new_stack = copy.copy(stack)
            for i in xrange(flipper_size):
                if new_stack[i] == '+':
                    new_stack[i] = '-'
                else:
                    new_stack[i] = '+'
            return 1 + solve(new_stack[1:], flipper_size)
        else:
            return -1000000000

T = int(sys.stdin.readline())

for N in xrange(T):
    S, K = sys.stdin.readline().strip().split(' ')

    flips = solve(list(S), int(K))

    print "Case #%d: %s" % (N + 1, flips >= 0 and str(flips) or 'IMPOSSIBLE')
