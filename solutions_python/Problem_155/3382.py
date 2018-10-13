# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 07:43:04 2015

@author: poonna
"""

def find_min_invites(audience):
    num_so_far = 0
    invites = 0
    for shyness in range(len(audience)):
        if shyness > num_so_far:
            invites += shyness - num_so_far
            num_so_far = shyness
        num_so_far += audience[shyness]
    return invites

num_tests = int(raw_input())
for i in range(num_tests):
    test = raw_input().split()
    audience = map(int, list(test[1]))
    invites = find_min_invites(audience)
    print("Case #" + str(i+1) + ": " + str(invites))
