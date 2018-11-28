#!/usr/bin/env python

import sys
import math

class Tokenizer():
    tokens = []

    def next(self):
        if len(self.tokens) == 0:
            self.tokens = sys.stdin.readline().split()
        return self.tokens.pop(0)


cin = Tokenizer()
cases = int(cin.next())

for i in xrange(cases):

    X = int(cin.next())
    R = int(cin.next())
    C = int(cin.next())

    #print X,R,C

    F = 'GABRIEL'
    NF = 'RICHARD'

    if (R*C) % X > 0:
        ans = NF
    else:
        p = R*C
        if X == 1:
            ans = F
        elif p == 1:
            if X > 1:
                ans = NF
            else:
                ans = F
        elif p == 2:
            if X > 2:
                ans = NF
            else:
                ans = F
        elif p == 3:
            ans = NF
            if X == 1:
                ans = F
        elif p == 6:
            ans = F
            if X > 3:
                ans = NF
        elif p == 9:
            if X == 1 or X == 3:
                ans = F
            else:
                ans = NF
        elif p == 16:
            if X == 3 or X > 4:
                ans = NF
            else:
                ans = F
        elif p == 12:
            ans = F
            if X > 4:
                ans = NF
        elif p == 8:
            ans = F
            if X >= 4:
                ans = NF
        elif p == 4:
            if R == 1 or C == 1:
                ans = F
                if X >= 3:
                    ans = NF
            else:
                ans = F
                if X >= 3:
                    ans = NF
    print("Case #" + str(i + 1) + ": " + str(ans))
