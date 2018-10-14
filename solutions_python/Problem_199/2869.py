#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ 2017 Qualification Round: Problem A"""


def flip(stack):
    stack_list = list(stack)
    new_stack_list = ['-' if pan == '+' else '+' for pan in stack_list]
    new_stack = ''.join(new_stack_list)
    return new_stack


def solve(stack, K):
    sol = 0

    i = 0
    while i < len(stack) - K + 1:
        pancake = stack[i]
        if pancake == '-':
            stack = stack[:i] + flip(stack[i:i+K]) + stack[i+K:]
            sol += 1
        i += 1

    if '-' in stack:
        sol = -1

    return sol


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        S, K_ = input().strip().split()
        K = int(K_)

        y = solve(S, K)
        if y == -1:
            y = "IMPOSSIBLE"

        print("Case #%d: %s" % (x+1, str(y)))
