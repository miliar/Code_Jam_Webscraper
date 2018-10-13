import re
from collections import defaultdict
import codejam

class Solver(codejam.CodeJam):

    data = (('V1', list, str),)

    def dosolve(self, case):
        clen = int(case.V1.pop(0))
        comb = {}
        for c in xrange(clen):
            full = case.V1.pop(0)
            old, new = full[:-1], full[-1]
            comb[old] = new
            comb[old[::-1]] = new

        dlen = int(case.V1.pop(0))
        antis = defaultdict(list)
        for d in xrange(dlen):
            i, j = case.V1.pop(0)
            antis[i].append(j)
            antis[j].append(i)

        elemlist = []
        for spell in case.V1[1]:
            elemlist.append(spell)
            last = ''.join(elemlist[-2:])
            if last in comb:
                elemlist[-2] = comb[last]
                del elemlist[-1]

            for i, pspell in enumerate(elemlist[:-1]):
                if pspell in antis[elemlist[-1]]:
                    elemlist = []
                    break

        return "[%s]" % ', '.join(elemlist)

s = Solver()
s.write()
