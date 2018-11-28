#!/usr/bin/python3
import sys, re
readline = sys.stdin.readline

N = int(readline())
for case in range(1, 1 + N):
    num = [int(digit) for digit in '0' + readline().strip()]
    num = num[::-1]
    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            new_i = min(d for d in num[:i] if d > num[i])
            tail = sorted(num[:i + 1], reverse=True)
            tail.remove(new_i)
            num[i] = new_i
            num[:i] = tail
            break
    num = num[::-1]
    print("Case #{0}: {1}".format(case, int(''.join(str(d) for d in num))))
