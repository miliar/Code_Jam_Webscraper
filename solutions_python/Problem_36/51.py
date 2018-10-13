from qhd.dec import memoized
import sys; sys.setrecursionlimit(10000)

def solve(haystack, needle):
    alphabet = frozenset(needle)
    haystack = filter(alphabet.__contains__, haystack)
    @memoized
    def _(haystack, needle):
        if haystack == '':
            return 0
        if len(needle) == 1:
            return haystack.count(needle) % 10000
        if haystack[0] != needle[0]:
            return _(haystack[1:], needle) % 10000
        return (_(haystack[1:], needle[1:]) + _(haystack[1:], needle)) % 10000
    return _(haystack, needle)

import sys
f = sys.stdin
next(f)
for X, line in enumerate(f, 1):
    print 'Case #%d: %04d' % (X, solve(line, 'welcome to code jam'))
