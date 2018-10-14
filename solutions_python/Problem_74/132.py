from collections import defaultdict
import codejam

class Solver(codejam.CodeJam):

    data = (('V1', list, str),)

    def dosolve(self, case):
        listdata = case.V1[1:]

        elapsed = defaultdict(int)
        lasts = {'O': 1, 'B': 1}
        seconds = last = 0
        for r, btn in (listdata[i:i+2] for i in xrange(0, len(listdata), 2)):
            other = 'B' if r == 'O' else 'O'
            btn = int(btn)
            dist = abs(lasts[r] - btn)
            dist = dist - elapsed[other] if dist > elapsed[other] else 0

            elapsed[r] += dist + 1
            lasts[r] = btn
            if last != r:
                seconds += elapsed[other]

            elapsed[other] = 0
            last = r

        return seconds + elapsed[r]

s = Solver()
s.write()

