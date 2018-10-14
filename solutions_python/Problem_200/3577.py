#!/usr/bin/env python3

import sys

def solve(case):
    n = input()
    o = list(n)

    turn = -1

    for i in range(len(o) - 1):
        if ord(o[i]) > ord(o[i + 1]):
            turn = i
            o[i] = str((ord(o[i]) - ORD - 1) % 10)
            #o[i] = chr(ord(o[i]) - 1)
            break

    for i in range(turn - 1, -1, -1):
        if ord(o[i]) > ord(o[i + 1]):
            turn = i
            o[i] = str((ord(o[i]) - ORD - 1) % 10)
            #o[i] = chr(ord(o[i]) - 1)

    sys.stdout.write("Case #{}: ".format(case + 1))

    is_zero = True
    for i in range(len(o)):
        is_zero = is_zero and (o[i] == '0') and (i <= turn)

        if is_zero:
            continue

        if (turn == -1 or i <= turn):
            sys.stdout.write(o[i])
        else:
            sys.stdout.write('9')

    sys.stdout.write('\n')
    sys.stdout.flush()

T = int(input())
ORD = ord('0')

for case in range(T):
    solve(case)
