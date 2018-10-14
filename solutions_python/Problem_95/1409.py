import os
import sys
import string
from pprint import pprint

from utils import stripped_lines, ints


def generate_translation(source, target):
    # remove all whitespace from example texts
    source, target = map(lambda t: ''.join(t.split()), (source, target))

    unused = set(string.lowercase)
    trans = dict((letter, None) for letter in string.lowercase)
    for s, t in zip(source, target):
        trans[s] = t
        unused.discard(t)

    # sort out letters that are still unknown
    for s, t in trans.items():
        if not t:
            trans[s] = unused.pop()

    return string.maketrans(''.join(trans.keys()), ''.join(trans.values()))

def solve_next_case(lines, trans):
    line = lines.next()
    return line.translate(trans)

def main():
    source = """
    ejp mysljylc kd kxveddknmc re jsicpdrysi
    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
    de kr kd eoya kw aej tysr re ujdr lkgc jv
    y qee
    """
    target = """
    our language is impossible to understand
    there are twenty six factorial possibilities
    so it is okay if you want to just give up
    a zoo
    """

    trans = generate_translation(source, target)

    fin_name = sys.argv[1]
    with open(fin_name) as fin:
        lines = stripped_lines(fin)

        numcases = int(lines.next())

        for caseno in range(1, numcases+1):
            result = solve_next_case(lines, trans)
            
            outstr = 'Case #%d: %s' % (caseno, result)
            print outstr

if __name__ == '__main__':
    main()