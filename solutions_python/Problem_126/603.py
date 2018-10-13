import re
import string # pylint: disable=W0402
import sys


EXAMPLE_IN = """\
4
quartz 3
straight 3
gcj 2
tsetse 2
"""

EXAMPLE_OUT = """\
Case #1: 4
Case #2: 11
Case #3: 3
Case #4: 11
"""

VOWELS = "aeiou"
CONSONANTS = "".join(c for c in string.lowercase if c not in VOWELS)

checkers = {} # pylint: disable=C0103
def make_verify(n):
    if n not in checkers:
        checkers[n] = re.compile('[' + CONSONANTS +  ']{%d}' % n).search
    return checkers[n]


def substr(s, n):
    length = len(s)
    for start in xrange(length-n+1):
        for end in xrange(start + n, length+1):
            yield s[start:end]



def substrings(s, n):
    p = make_verify(n)
    for x in substr(s, n):
        if p(x):
            yield x

def solve(name, n):
    print >> sys.stderr, '### solving', name, n
    return sum(1 for _ in substrings(name, n))


def main(lines):
    for i in xrange(int(next(lines))):
        name, n_str = next(lines).split()
        n = int(n_str)
        ans = 'Case #%d: %d' % (i+1, solve(name, n))
        print >> sys.stderr, ans
        print ans



#    test_cases = [lines[i*4for i in range(cases)]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = iter(EXAMPLE_IN.split('\n'))
    else:
        input = open(sys.argv[1])

    main(input)
