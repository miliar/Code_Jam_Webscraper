#!/usr/bin/env python
#
# Author    : Mahendra Chintomby (mchintomby@gmail.com)
#
"""
"""
import cStringIO
import fileinput
import itertools
import operator


def patrick_sum(vals):
    """
    >>> patrick_sum([5, 4])
    1
    >>> patrick_sum([7, 9])
    14
    >>> patrick_sum([50, 10])
    56
    >>> patrick_sum([1, 2, 1])
    2
    >>> patrick_sum([1, 3, 1])
    3
    """
    return reduce(operator.__ixor__, vals) 
        
def candy_splitting(infile=None):
    if infile is None:
        infile = fileinput.input()

    def get_lines(n):
        lines = list()
        for i in xrange(n):
            lines.append(infile.readline())
        return lines

    def get_max_candy(count, values):
        def pile_gen():
            for i in xrange(1, count):
                for j in itertools.combinations(values, i):
                    l = list(values)
                    for k in j:
                        l.remove(k)
                    yield (j, tuple(l))

        pg = pile_gen()
        max_pile = 0
        for p1, p2 in pg:
            if patrick_sum(p1) == patrick_sum(p2):
                max_pile = max(sum(p1), max_pile)

        return max_pile or 'NO'

    try:
        cases = int(infile.readline())
    except ValueError:
        print 'Error: Test case count not found'
        return []
    case_results = list()
    for case in xrange(cases):
        lines = get_lines(2)
        case_results.append('Case #%d: %s' % (case+1, 
                    get_max_candy(int(lines[0]), 
                        [int(i) for i in lines[1].split(' ')])))
    return case_results

def test():
    expected = [
        'Case #1: NO',
        'Case #2: 11',
        'Case #3: 5',
        'Case #4: 9',
        'Case #5: 4356',
    ]

    result = candy_splitting(cStringIO.StringIO(
        '5\n'
        '5\n'
        '1 2 3 4 5\n'
        '3\n'
        '3 5 6\n'
        '2\n'
        '5 5\n'
        '3\n'
        '1 4 5\n'
        '3\n'
        '250 2149 2207\n'
    ))

    print '\n'.join(result)
    assert expected == result, expected

if __name__ == "__main__":
    print '\n'.join(candy_splitting())
