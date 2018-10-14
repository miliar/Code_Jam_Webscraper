from __future__ import with_statement
import sys

welcome = "welcome to code jam"
letters = set(welcome)

def check(i, lst):
    tmp = welcome[i]
    if tmp not in lst:
        return 0
    gen = [j for j, c in enumerate(lst) if c == tmp]
    if i == len(welcome)-1:
        return len(gen)
    return sum((check(i+1, lst[j:]) for j in gen))

with open(sys.argv[1]) as f:
    num_cases = int(f.readline())

    for case in xrange(num_cases):
        line = f.readline().strip()
        line = ''.join((i for i in line if i in letters))

        print "Case #%d: %04d" % (case+1, check(0, line) % 10000)
