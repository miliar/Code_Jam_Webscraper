#!/usr/bin/env pypy
import sys

# should use ordered set for quick lookups
KNOWN_TIDY = set()
# KNOWN_UNTIDY = set()


def is_tidy_number(number):
    # Check cache
    if number in KNOWN_TIDY:
        return True, 0
    # Calculate if we don't know
    numstr = str(number)
    maxlen = len(numstr)
    for i in range(1, maxlen):
        if ord(numstr[i]) < ord(numstr[i - 1]):
            can_skip_raw = numstr[i: maxlen]
            can_skip = int(''.join(can_skip_raw))
            return False, can_skip
    KNOWN_TIDY.add(number)
    return True, 0


class Case(object):

    def __init__(self, idx, start):
        self.idx = int(idx)
        self.start = int(start)

    def __str__(self):
        return "Case #%i: %i" % (self.idx, self.tidy)

    def __repr__(self):
        return "<Case instance at %i: #%i %i>" % (id(self), self.idx, self.tidy)

    @property
    def tidy(self):
        next = self.start
        while True:
            check, skip = is_tidy_number(next)
            if check:
                return next
            elif next == -1:
                print("WE DIDN'T FIND ANY TIDY NUMBER !!!!")
                break
            else:
                next -= skip
            next -= 1
        return next


def read_cases(file):
    cases = []
    with open(file) as f:
        cases_raw = int(f.readline())
        for idx in range(1, cases_raw+1):
            number = f.readline()
            cases.append(Case(idx, number))
    return cases


if __name__ == '__main__':
    cases = read_cases(sys.argv[1])
    for case in cases:
        print(case)
