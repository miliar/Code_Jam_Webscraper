# -*- coding: utf-8 -*-
from collections import deque
from itertools import combinations

with file("B-large-0.in") as inp:
    with file("B-large-0.out", "w") as outp:
        n = int(inp.readline().strip())
        for i in xrange(n):
            combs = {}
            oppos = set()
            elems = deque()
            raw_seq = inp.readline().strip().split()
            combs_offset = 0
            combs_n = int(raw_seq[combs_offset])
            for j in xrange(combs_n):
                a, b, c = raw_seq[1 + combs_offset + j]
                combs[(a, b)] = combs[(b, a)] = c
            oppos_offset = combs_offset + combs_n + 1
            oppos_n = int(raw_seq[oppos_offset])
            for j in xrange(oppos_n):
                a, b = raw_seq[1 + oppos_offset + j]
                oppos.add((a, b))
                oppos.add((b, a))
            elemseq_offset = oppos_offset + oppos_n + 1
            for elem in raw_seq[elemseq_offset + 1]:
                elems.append(elem)
                while len(elems) > 1:
                    last = elems.pop()
                    prev = elems.pop()
                    combo = combs.get((last, prev), False)
                    if combo:
                        elems.append(combo)
                    else:
                        elems.append(prev)
                        elems.append(last)
                        break
                if any((combo in oppos) for combo in combinations(elems, 2)):
                    elems = deque()
            result = ", ".join(elems)
            outp.write("Case #%s: [%s]\n" % (i+1, result))


