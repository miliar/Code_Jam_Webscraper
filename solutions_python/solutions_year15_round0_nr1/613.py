# Qualification Round 2014
# Problem A. Magic Trick
# MichelJ

import sys
import logging
import StringIO
from itertools import chain

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

def solve(smax, ns):
    add = 0
    standing = 0
    for i in xrange(smax + 1):
        while standing < i:
            add += 1
            standing += 1
        standing += ns[i]
    return str(add)
    
def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        smax, s = raw_input().split(' ')
        smax = int(smax)
        ns = [int(s[i]) for i in xrange(smax+1)]
        print 'Case #%d: %s' % (tc, solve(smax, ns))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""4
4 11111
1 09
5 110011
0 1
"""


# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")
