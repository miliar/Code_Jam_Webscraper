#!/usr/bin/env python
def solve(line):
    s_max, S = line.split()
    ans, stood_up = 0, 0
    for req, s in enumerate(S):
        s = int(s)
        if req > stood_up:
            ans += req - stood_up
            stood_up += req - stood_up
        stood_up += s
    return ans

case_num = input()
for case in range(1, case_num + 1):
    line = raw_input()
    print("Case #%i: %i" % (case, solve(line)))

