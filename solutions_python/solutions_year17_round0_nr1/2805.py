#!/usr/bin/env python3

num_cases = int(input())

flipper = {'+': '-',
           '-': '+'}

for case in range(1, num_cases+1):
    s, k = input().split()
    s = list(s)
    k = int(k)

    num_flip_positions = len(s) - k + 1

    num_flips = 0
    for idx in range(num_flip_positions):
        if s[idx] == '-':
            num_flips += 1
            s[idx:idx+k] = [flipper[p] for p in s[idx:idx+k]]

    if '-' in s[-k:]:
        answer = "IMPOSSIBLE"
    else:
        answer = num_flips

    print("Case #{case}: {answer}".format(case=case, answer=answer))
