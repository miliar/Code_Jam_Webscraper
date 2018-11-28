#!/usr/bin/env python

import sys

def check(answer, cards):
    return set(cards[int(answer) - 1].strip().split(" "))

data = sys.stdin.readlines()

total_cases = int(data.pop(0));
for i in range(0, total_cases):
    cases = data[i * 10: (i * 10) + 10]
    ans = []
    for j in range(0, 2):
        temp = cases[j * 5: (j * 5) + 5]
        ans.append( check(temp[0], temp[1:]) )

    r = ans[0] & ans[1]
    l = len(r)
    t = "Case #%d: " % (i + 1)
    if l == 1:
        print t + str(r.pop())
    elif l < 1:
        print t + "Volunteer cheated!"
    else:
        print t + "Bad magician!"
       
