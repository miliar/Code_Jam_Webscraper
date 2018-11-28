#!/usr/bin/python3

import sys

def solve(n):
    result = []
    number = str(n)
    fillup = False

    for i in range(len(number)):
        cand = number[i]
        result.append(cand)
        if i < len(number)-1 and number[i+1] < cand:
            lesser = str(int(cand) - 1)
            subst = None
            for j in range(len(result)):
                if result[j] == cand:
                    result[j] = lesser
                    subst = j
                    break

            result = result[0:j+1]
            fillup = True
            break

    if fillup:
        result += ['9'] * (len(number) - len(result))

    return int(''.join(result))


T = int(sys.stdin.readline().strip())

for t in range(T):
    S = sys.stdin.readline().strip()
    print("Case #{}: {}".format(t+1, solve(S)))

