import sys
import re

class Teed(object):
    """Wraps a file object. It behaves mostly like the original one,
     but the calls to "write" are replicated to stdout.

     The writelines method is not overriden yet.
     """

    def __init__(self, original):
        self._orig = original

    def write(self, str):
        sys.stdout.write(str)
        self._orig.write(str)

    def __getattr__(self, property):
        """Delagate all other properties
           and method calls to wrapped object"""
        return self._orig.__getattribute__(property)

def main():
    name = re.match(r"^(.*\.)in$", sys.argv[1]).group(1) + "out"

    with open(sys.argv[1]) as f:
        orig_out = sys.stdout
        with open(name, "w") as out_f:
            wrapped = Teed(out_f)
            parse(f, wrapped)

def parse(inp, out):
    cases = int(inp.next().strip())
    for i in range(cases):
        c = parse_case(inp)
        print "Solving case #%d (%s)" % (i + 1, c)
        solution = solve(c)
        print >> out, "Case #%d: %s" % (i + 1, solution)

from itertools import imap, groupby
from functools import reduce
import operator


def parse_case(inp):
    d = int(inp.next())
    diners = map(int, inp.next().split())
    assert d == len(diners)
    return diners

def solve(diners):
    inp = counts(diners)

    level = inp[0][0]
    minutes = level
    found_min = False
    while level > 2:
        next_level, next_minutes = comp_next(level, inp)
        # print next_level, next_minutes

        # if next_minutes > minutes and next_minutes < inp[0][0]:
        #     return minutes

        level = next_level
        minutes = min(minutes, next_minutes)
    return minutes

def comp_next(level, diners):
    next_level = level - 1
    minutes = 0
    for n, p in diners:
        if n > next_level:
            minutes += p * (-(-n / next_level) - 1) # integer ceil division
        else:
            break
    return next_level, minutes + next_level

def counts(diners):
    c = {}
    for d in diners:
        c[d] = c.get(d, 0) + 1

    return sorted(c.iteritems(), reverse=True)

if __name__ == "__main__":
    main()
