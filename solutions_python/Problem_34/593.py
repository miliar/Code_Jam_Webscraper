from sys import stdin
from sys import stdout
import re

inp = stdin.read().split()
d = int(inp[1])

words = inp[3:d+3]
cases = inp[d+3:]

case = 0
for pattern in cases:
    p = "^" + pattern.replace("(", "[").replace(")", "]") + "$"
    k = len([w for w in words if re.match(p, w)])
    case = case + 1
    print "Case #%d: %d" % (case, k)