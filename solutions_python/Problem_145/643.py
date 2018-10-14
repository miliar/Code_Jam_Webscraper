__author__ = 'Shailesh'

from fractions import Fraction
import math

with open("../files/A-small-attempt0.in", 'r') as inp, open("../files/outputA.txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i+1) + ": "
        p, q = map(int, inp.readline().split('/'))
        f = Fraction(p, q)
        if f.denominator == 0 or f.denominator & (f.denominator - 1) != 0:
            out.write(string + "impossible\n")
            continue
        answer = int(math.log(f.denominator, 2))
        if answer > 40:
            out.write(string + "impossible\n")
            continue

        result = int(math.ceil(math.log(1/f, 2)))
        out.write(string + str(result) + "\n")


