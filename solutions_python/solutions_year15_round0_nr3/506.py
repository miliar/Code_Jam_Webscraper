# Qualification Round 2015
# Problem C. Dijkstra
# MichelJ

import sys
import logging
import StringIO
from itertools import *

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

combine = { "11":"1", "1i":"i", "1j":"j", "1k":"k",
            "i1":"i", "ii":"-1", "ij":"k", "ik":"-j",
            "j1":"j", "ji":"-k", "jj":"-1", "jk":"i",
            "k1":"k", "ki":"j", "kj":"-i", "kk":"-1",
            "-11":"-1", "-1i":"-i", "-1j":"-j", "-1k":"-k",
            "-i1":"-i", "-ii":"1", "-ij":"-k", "-ik":"j",
            "-j1":"-j", "-ji":"k", "-jj":"1", "-jk":"-i",
            "-k1":"-k", "-ki":"-j", "-kj":"i", "-kk":"1" }

def is_ijk(s):
    if len(s)<3:
        return "NO"
    ls = len(s)
    break1 = 1
    s1 = s[0]
    while break1 < ls - 1:
        if s1 == "i":
            break2 = break1 + 1
            s2 = s[break1]
            while break2 < ls:
                if s2 == "j":
                    s3 = s[break2]
                    for i in xrange(break2+1,ls): # c in s[break2+1:]:
                        s3 = combine[s3+s[i]]
                    if s3 == "k":
                        return "YES"
                    return "NO"
                s2 = combine[s2+s[break2]]
                break2 += 1
        s1 = combine[s1+s[break1]]
        break1 += 1
    return "NO"


def solve(L, X, s):
    sx = s * X
    return is_ijk(sx)
    
def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        (L,X) = map(int, raw_input().split(' '))
        s = raw_input()
        print 'Case #%d:%s' % (tc, solve(L, X, s))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i
"""


# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")
