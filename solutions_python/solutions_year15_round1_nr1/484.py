#!/usr/bin/python
# vi: set fileencoding=utf-8 :

def eaten_minimum_number(m):
    method_1 = 0
    max_rate = 0
    for i in range(len(m) - 1):
        diff = m[i] - m[i + 1]
        if diff > 0:
            method_1 += diff
        max_rate = max(max_rate, diff)
    method_2 = 0
    for i in range(len(m) - 1):
        if m[i] <= max_rate:
            method_2 += m[i]
        else:
            method_2 += max_rate
            #rest += m[i] - max_rate
    return method_1, method_2


T = int(raw_input())
for case_number in range(1, T + 1):
    N = int(raw_input())
    m = map(int, raw_input().split())
    m1, m2 = eaten_minimum_number(m)
    print 'Case #%d: %d %d' % (case_number, m1, m2)
