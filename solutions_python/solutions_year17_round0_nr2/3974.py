#!/bin/python

import sys, math


def to_str(number):
    if len(number) == 1 and number[0] == '0':
        return '0'
    return ''.join(number).lstrip('0')

def get_largest_tidy(number):
    cur = 0
    prev = None

    while not prev or (cur < len(number) and prev <= number[cur]):
        prev = number[cur]
        cur += 1

    if cur == len(number):
        return number

    cur2 = cur + 1

    #print "num: {}, cur: {}".format(number, cur)

    while cur2 < len(number):
        number[cur2] = '9'
        cur2 +=1

    #print "num: {}, cur: {}".format(number, cur)

    while cur > 0  and number[cur - 1] > number[cur]:
        prev = int(number[cur - 1])
        number[cur - 1] = str(prev - 1)
        number[cur] = '9'
        cur -= 1


    #print "num: {}, cur: {}".format(number, cur)
    return number


num_cases = input()
for i in xrange(num_cases):
    number = raw_input()
    print "Case #{}: {}".format(i + 1, to_str(get_largest_tidy(list(number))))
