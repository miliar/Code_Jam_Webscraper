#!/usr/bin/env python

import sys


def elist(l):
    r = '['
    if len(l):
        for e in l:
            r += e + ', '
        r = r[:-2]
    r += ']'
    return r

def case(line):
    i = 0
    data = line.strip().split()

    combinations = []
    num = int(data[i])
    i += 1
    if num > 0:
        combinations.extend(list(c) for c in data[i:i+num])
        i += num

    def combines(tail):
        for c in combinations:
            if c[0] in tail and c[1] in tail:
                if c[0] == c[1] and c[:2] != tail:
                    return False
                return c[2]
        return False

    oppositions = []
    num = int(data[i])
    i += 1
    if num > 0:
        oppositions.extend([list(o) for o in data[i:i+num]])
        i += num

    def has_opposition(out):
        for o in oppositions:
            if o[0] in out and o[1] in out:
                return True
        return False

    def check(e, out):
        out.append(e)
        rep = combines(out[-2:])
        if rep:
            del out[-2:]
            out.append(rep)
        if not rep and has_opposition(out):
            del out[0:]

    el_out = []
    el_in = list(data[i+1])
    for e in el_in:
        check(e, el_out)

    return elist(el_out)


if __name__ == "__main__":
    f = open(sys.argv[1])
    numcases = int(f.readline().strip())
    for i in range(numcases):
        print "Case #%d: %s" % (i + 1, case(f.readline().strip()))

