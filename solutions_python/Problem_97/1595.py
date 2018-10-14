#!/usr/bin/env python
#
# Author    : Mahendra Chintomby (mchintomby@gmail.com)
#
"""
"""
import cStringIO
import fileinput
import collections


def do(infile=None):
    if infile is None:
        infile = fileinput.input()

    def work(line):
        a, b = line.strip().split()
        a = int(a)
        b = int(b)
        count = 0
        for n in xrange(a, b):
            str_n = str(n)
            len_n = len(str_n)
            seen = set()
            for i in xrange(1, len_n):
                m = str_n[i:] + str_n[:i]
                m = int(m)
                str_m = str(m)
                if len(str_m) != len_n:
                    continue
                if not (n < m and m <= b):
                    continue
                pair = tuple(sorted((n,m)))
                if pair in seen:
                    continue
                seen.add(pair)
                count += 1

        return count

    def get_lines(n):
        lines = list()
        for i in xrange(n):
            lines.append(infile.readline())
        return lines

    try:
        cases = int(infile.readline())
    except ValueError:
        print 'Error: Test case count not found'
        return []

    case_results = list()
    for case in xrange(cases):
        lines = get_lines(1)
        case_results.append('Case #%d: %s\n' % (case+1, work(''.join(lines))))
    return case_results

def test():
    expected = [
        'Case #1: 0\n',
        'Case #2: 3\n',
        'Case #3: 156\n',
        'Case #4: 287\n',
    ]

    result = do(cStringIO.StringIO(
        '4\n'
        '1 9\n'
        '10 40\n'
        '100 500\n'
        '1111 2222\n'
    ))

    print ''.join(result)
    assert expected == result, expected

if __name__ == "__main__":
    #test()
    print ''.join(do())
