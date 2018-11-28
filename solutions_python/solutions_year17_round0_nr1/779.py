#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IPython import embed

def replace_after_zero(d):
    for i in range(len(d)):
        if d[i] == 0:
            d[i-1]-=1
            idx = i
            while idx < len(d):
                d[idx]=9
                idx+=1
    return d

def d2l(x):
    return [int(x) for x in str(cipher)]

def l2d(numList):
    return int(''.join(map(str,numList)))

def flip_char(a):
    if a=='+':
        return '-'
    if a=='-':
        return '+'

def solve(d, K):
    d = list(d)

    if is_tidy(d):
        return 0

    i=0
    c = 0 # counter
    while i <= (len(d)-K):
        if d[i] != '+':
            c+=1
            idx = 0
            while idx < K:
                d[i+idx] = flip_char(d[i+idx])
                idx+=1
        i+=1

    return c if is_tidy(d) else 'IMPOSSIBLE'


def is_tidy(d):
    for i in range(len(d)):
        if d[i] != '+':
            return False
    return True

if __name__ == "__main__":
    testcases = input()
    #testcases = ['---+-++- 3', '+++++ 4', '-+-+- 1']
    #K = 1
    #t = int(raw_input())

    for caseNr in xrange(1, testcases+1):
    #for caseNr in xrange(1, len(testcases)+1):
        #cipher = testcases[caseNr-1]
        #cipher = raw_input()
        cipher, K = [s for s in raw_input().split(" ")]
        #cipher, K = [s for s in cipher.split(" ")]
        K = int(K)

        #print(cipher)
        print("Case #%i: %s" % (caseNr, solve(cipher, K)))
