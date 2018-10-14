#!/usr/local/bin/python
import sys

def solve():
    line = sys.stdin.readline().strip()
    digits = [int(c) for c in list(line)][::-1]
    answer = 0

    for i in range(len(digits)):
        hasInversion = False
        for j in range(i, len(digits)-1):
            if digits[j+1] > digits[j]:
                hasInversion = True
                break
        if hasInversion:
            digits[i] = 9
            digits[i+1] -= 1
        answer += pow(10, i) * digits[i]
    return answer

cases = int(sys.stdin.readline())
for case in range(cases):
    print "Case #{}: {}".format(case+1, solve())
