#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    inputs = cipher.split()
    max_shyness = inputs[0]
    accum = 0
    invites = 0
    for shyness, num in enumerate (inputs[1]):
        if accum < shyness:
            new_invite = shyness - accum
            invites += new_invite
            accum += new_invite + int(num)
        else:
            accum += int(num)
    return invites

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
