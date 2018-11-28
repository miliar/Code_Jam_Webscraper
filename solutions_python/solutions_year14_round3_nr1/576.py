import sys
import math
from fractions import Fraction
#####


def getGeneration():
    unsplitted = raw_input()
    frac = Fraction(unsplitted)
    denom = frac.denominator
    ans = math.log(float(1/frac),2)
    intans = int(math.ceil(ans))
    num = int(denom)
    if num != 0 and ((num & (num - 1)) == 0):
        return intans
    else:
        return "impossible"


######



sys.stdin = open("large.in", "r")

sys.stdout = open("A-large.out", "w")
no = input()
for i in xrange(0,no):
    print "Case #{0}:".format(i+1),
    print getGeneration()

sys.stdout.close()
