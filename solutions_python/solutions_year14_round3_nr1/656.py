from jam import jam
from fractions import Fraction as frac
import math

# jam.startDebugging()

# parse input
jam.read('A-small-attempt0.in')
numCases = int(jam.state.pop(0))
cases = []
for _ in range(numCases):
    p, q = map(int, jam.state.pop(0).split('/'))
    cases.append(frac(p,q))

def gens(f):
    mag = math.log(f._denominator, 2)
    if mag != int(mag): # not a power of 2
        result = "impossible"
    else:
        for n in range(1,40):
            g = f - frac(1, 2**n)
            if g < 0:
                continue
            else:
                break
        return n
    return result

for caseNum, f in enumerate(cases):
    print "Case #{}: {}".format(caseNum+1, gens(f))
