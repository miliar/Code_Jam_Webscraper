#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from collections import Counter

import sys

sys.stdin.readline()

def invoke(invokelst, combos, opposed):
    curinvokation = []
    invoked = Counter()
    for e in invokelst:
        curinvokation.append(e)
        last = tuple(curinvokation[-2:])
        if last in combos:
            assert len(last) == 2
            curinvokation[-2:] = combos[last]
            invoked[last[0]] -= 1
        else:
            suspect = opposed.get(e, None)
            if suspect is not None and invoked & suspect:
                curinvokation = []
                invoked = Counter()
                continue
        invoked[curinvokation[-1]] += 1
    return curinvokation

def main():
    for case,line in enumerate(sys.stdin):
        fields = iter(line.strip().split())
        combocount = int(fields.next())

        combos = {}
        for _ in xrange(combocount):
            c = fields.next()
            assert len(c) == 3
            combos[tuple(c[:2])] = c[2]
            combos[tuple(reversed(c[:2]))] = c[2]

        oppocount = int(fields.next())
        oppos = {}
        for _ in xrange(oppocount):
            o = fields.next()
            assert len(o) == 2
            oppos.setdefault(o[0], set()).add(o[1])
            oppos.setdefault(o[1], set()).add(o[0])
        for k in oppos:
            oppos[k] = Counter(oppos[k])
        fields.next()
        invokelst = fields.next()
        invokation = invoke(invokelst, combos, oppos)
        answer = ', '.join(invokation)
        print "Case #%d: [%s]" % (case + 1, answer)

if __name__ == '__main__':
    main()
