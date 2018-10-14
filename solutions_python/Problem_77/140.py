from collections import defaultdict
import codejam

class Solver(codejam.CodeJam):

    data = (('V1', tuple, int),)

    def dosolve(self, case):
        V1sorted = sorted(case.V1)
        lV1 = len(case.V1)
        wrongs = len([i for i in xrange(lV1) if V1sorted[i] != case.V1[i]])
        return "%d.000000" % wrongs


s = Solver()
s.write()
