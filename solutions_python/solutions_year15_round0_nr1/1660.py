#!/usr/bin/env python

import sys

class Tokenizer():
    tokens = []

    def next(self):
        if len(self.tokens) == 0:
            self.tokens = sys.stdin.readline().split()
        return self.tokens.pop(0)

cin = Tokenizer()
cases = int(cin.next())

for i in range(cases):

    Smax = cin.next()

    s = cin.next();

    friends = 0

    sums = 0

    for idx, si in enumerate(s):
        su = sums

        sums = su+int(si)

        if su + friends < idx:
            friends += idx-su-friends

    ans = friends

    print("Case #" + str(i + 1) + ": " + str(ans))
