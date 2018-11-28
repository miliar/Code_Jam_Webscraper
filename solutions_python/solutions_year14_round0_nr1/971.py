#!/usr/bin/env python

import sys
import math

def get_choices():
    choices = None
    row = int(sys.stdin.readline());
    for i in xrange(4):
        nums = [int(x) for x in sys.stdin.readline().split()]
        if (i + 1) == row:
            choices = set(nums)

    return choices

T = int(sys.stdin.readline())

for caseno in xrange(T):
    choices_A = get_choices()
    choices_B = get_choices()

    answer = list(choices_A & choices_B)

    ans = None

    if len(answer) == 0:
        ans = "Volunteer cheated!"
    elif len(answer) > 1:
        ans = "Bad magician!"
    else:
        ans = str(answer[0])

    print "Case #%d: %s" % (caseno + 1, ans)


