
from itertools import permutations

import sys

# parse tree
with open(sys.argv[1]) as input:
    cases = input.readline().strip()
    for i in xrange(int(cases)):
        num = input.readline().strip()
        num = num.replace(' ', '')
        onum = num
        try:
            while True:
                for permute in (''.join(x) for x in permutations(sorted(num))):
                    if int(permute) > int(onum):
                        print "Case #%s: %s" % (i+1, permute)
                        raise Exception
                num += '0'
        except Exception:
            pass


