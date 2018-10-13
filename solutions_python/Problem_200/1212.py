import sys
import numpy as np
sys.stdin = open('input.in', 'r')
sys.stdout = open('output.out', 'w')


def output(s):
    ind = len(s) - 1

    while ind > 0:
        if int(s[ind]) < int(s[ind - 1]):
            s[ind - 1] = int(s[ind - 1]) - 1 if int(s[ind - 1]) > 0 else 9

            for i in range(ind, len(s)):
                s[i] = 9

        ind -= 1

    for i in range(len(s)):
        if int(s[0]) == 0:
            s.pop(0)

            if len(s) == 0:
                break

    for i in range(len(s)):
        s[i] = str(s[i])

    return ''.join(s)

T = int(input())

for i in range(T):
    N = input()
    print("Case #" + str(i+1) + ": " + str(output(list(N))))
