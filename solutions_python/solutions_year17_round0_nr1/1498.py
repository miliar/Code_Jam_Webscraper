#! /usr/bin/env python
cases = int(raw_input())
for case in range(0, cases):
    s = raw_input().split(' ')

    p = list(s[0])
    n = int(s[1])
    f = 0

    for i in range(0, len(p)):
        if i <= len(p) - n:
            if p[i] == '-':
                for x in range(0, n):
                    if p[i+x] == '-':
                        p[i+x] = '+'
                    else:
                        p[i+x] = '-'
                f = f + 1
    done = True
    for c in p:
        if c != '+':
            done = False
    if done:
        print("Case #{}: {}".format(case + 1, f))
    else:
        print("Case #{}: {}".format(case + 1, "IMPOSSIBLE"))
