#! /usr/bin/python
'''
Splitting candy
'''

import operator

T = int(raw_input())

for i in range(T):
    C = int(raw_input())
    candies = map(int, raw_input().split())
    candies = sorted(candies)
    answer = reduce(operator.xor, candies, 0)
    if answer:
        answer = "NO"
    else:
        answer = reduce(operator.add, candies[1:], 0)
        
    print "Case #%d: %s" % (i + 1, answer)

    
