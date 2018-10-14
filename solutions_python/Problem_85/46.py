import sys
import codejam
from itertools import cycle

class Solver(codejam.CodeJam):

    def solve(self):
        fileobj = open(sys.argv[1])
        self.cases = int(fileobj.readline()[:-1])
        for i in xrange(self.cases):
            obj = codejam.Parsed()
            full = map(int, fileobj.readline().strip().split())
            obj.L, obj.t, obj.N, obj.C = full[:4]
            obj.spaces = full[4:]

            yield self.dosolve(obj)

    def dosolve(self, case):
        t = 0
        mult = 2
        built = 0
        d = 0
        totalD = 0
        spaces = []
        until_first_boost = int(case.t * 0.5)

        firstused = False

        i = 0
        for j, space in enumerate(cycle(case.spaces)):
            totalD += space

            if totalD > until_first_boost and not firstused:
                remain = totalD - until_first_boost
                space_p = space - remain

                spaces.append((space_p, False))
                spaces.append((remain, True))
                i += 2

                firstused = True
            else:
                spaces.append((space, totalD > until_first_boost))

            if case.N - 1 == j:
                break

        spaces.sort(reverse=True)

        built = 0
        for space, canuse in spaces:
            if canuse and built < case.L:
                t += space
                built += 1
            else:
                t += 2 * space
        
        return int(t)


s = Solver()
s.write()
