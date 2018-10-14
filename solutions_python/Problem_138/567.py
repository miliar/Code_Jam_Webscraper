# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 12:29:40 2014

@author: poonna
"""

def solve(n, a, b):
    count = 0
    i, j = 0, 0
    while (i < n) and (j < n):
        while (j < n) and (a[i] > b[j]):
            j = j + 1
        if j < n:
            count = count + 1
        i = i + 1
        j = j + 1
    return count

#n = 3
#a = [0.5, 0.1, 0.9]
#b = [0.6, 0.4, 0.3]

#n = 9
#a = [0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
#b = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458]

num_tests = int(raw_input())
for i in range(num_tests):
    n = int(raw_input())
    a = map(float, raw_input().split())
    b = map(float, raw_input().split())

    a.sort()
    b.sort()

    print 'Case #' + str(i+1) + ':',
    print str(solve(n, b, a)), str(n - solve(n, a, b))
