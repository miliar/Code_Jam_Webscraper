import re
from collections import defaultdict
import codejam

def bsum(array):
    res = 0
    for elem in array:
        res ^= elem
    return res

class Solver(codejam.CodeJam):

    data = (('V1', tuple, int),)

    def dosolve(self, case):
        if bsum(case.V1) != 0: return "NO"

        case.V1.sort(reverse=True)
        maxs = 0
        for i in xrange(1, len(case.V1)):
            bag1 = case.V1[:i]
            bag2 = case.V1[i:]

            if bsum(bag1) == bsum(bag2):
                maxs = max(sum(bag1), sum(bag2),  maxs)

        return maxs

s = Solver()
s.write()

