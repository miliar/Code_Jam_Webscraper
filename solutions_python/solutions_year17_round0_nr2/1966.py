#!/usr/bin/env python
# encoding: utf-8

'''
tidy_numbers.py
Created by Shuailong on 2017-04-08.
https://code.google.com/codejam/contest/3264486/dashboard#s=p1
'''

T = int(raw_input())
for case in xrange(1, T + 1):
    N = list(raw_input())
    i = 0
    while i < len(N)-1:
        if N[i] > N[i+1]:
            N[i] = str(int(N[i])-1)
            if i >= 1 and N[i-1] > N[i]:
                i -= 1
                continue
            for j in range(i+1, len(N)):
                N[j] = '9'
            break
        i += 1
    N = ''.join([i for i in N if i != '0'])

    print "Case #{}: {}".format(case, N)
