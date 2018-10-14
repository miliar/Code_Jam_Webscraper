#!/usr/bin/env python
import sys
import math

argv = sys.argv
argc = len(argv)

inp = argv[1]

def process_string(s):
    tokens = []

    sub = ""
    last_char = s[0]

    for c in s:
        if c == last_char:
            sub += c
        else:
            last_char = c
            tokens.append(sub)
            sub = str(c)
    tokens.append(sub)

    return tokens

def do_problem(stringA, stringB):
    if stringA == stringB:
        return 0

    pA = process_string(stringA)
    pB = process_string(stringB)

    if len(pA) != len(pB):
        return "Fegla Won"
    for i in range(len(pA)):
        if pA[i][0] != pB[i][0]:
            return "Fegla Won"

    actions = 0
    for i in range(len(pA)):
        actions += abs(len(pA[i]) - len(pB[i]))

    return actions

with open(inp) as f:
    T = int(f.readline())

    for i in range(T):
        N = int(f.readline())

        strings = [f.readline().strip() for _ in range(N)]
        answer = do_problem(strings[0], strings[1])

        print("Case #{}: ".format(i+1) + str(answer))
