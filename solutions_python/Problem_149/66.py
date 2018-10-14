#!/usr/bin/env python

def solve(elements, num):
    sorted_elements = sorted(elements)
    count = 0
    for elem in sorted_elements:
        i = elements.index(elem)
        end = num - i - 1
        count += min(i, num - i - 1)
        elements.remove(elem)
        num -= 1
    print count

for case in xrange(int(raw_input())):
    print "Case #%d:" % (case+1),
    num = int(raw_input())
    elements = map(int, raw_input().split())
    solve(elements, num)
