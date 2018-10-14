#!/usr/bin/env python

import sys
import math

class Tokenizer():
    tokens = []

    # pass True to return string
    def next(self, is_string=False):
        if len(self.tokens) == 0:
            self.tokens = sys.stdin.readline().split()
        if not is_string:
            return int(self.tokens.pop(0))
        return self.tokens.pop(0)



cin = Tokenizer()
cases = cin.next()
#print("cases : " + str(cases))

for i in range(cases):

    # Variables for each case here
    row1 = cin.next() - 1
    # Get list from line
    d1 = [[cin.next() for x in range(4)] for y in range(4)]
    row2 = cin.next() - 1
    d2 = [[cin.next() for x in range(4)] for y in range(4)]

    r = set(d1[row1]) & set(d2[row2])

    if len(r) == 1:
        print("Case #" + str(i + 1) + ": " + str(list(r)[0]))
    elif len(r) > 1:
        print("Case #" + str(i + 1) + ": Bad magician!")
    elif len(r) == 0:
        print("Case #" + str(i + 1) + ": Volunteer cheated!")
