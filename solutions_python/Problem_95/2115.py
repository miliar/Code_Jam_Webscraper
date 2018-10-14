#!/usr/bin/env python
#
# Author    : Mahendra Chintomby (mchintomby@gmail.com)
#
"""
"""
import cStringIO
import fileinput

def make_mapping():
    a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    b = 'our language is impossible to understand'
    c = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    d = 'there are twenty six factorial possibilities'
    e = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    f = 'so it is okay if you want to just give up'
    mapping = {
        'y': 'a',
        'e': 'o',
        'q': 'z',
        'z': 'q',
    }
    for l in [zip(a,b), zip(c, d), zip(e,f)]:
        mapping.update(dict(l))
    return mapping

MAPPING = make_mapping()

def do(infile=None):
    if infile is None:
        infile = fileinput.input()

    mapping = MAPPING
    def work(line):
        ret = []
        for c in line:
            ret.append(mapping.get(c, c))
        return ''.join(ret)

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
        case_results.append('Case #%d: %s' % (case+1, work(''.join(lines))))
    return case_results

def test():
    expected = [
        'Case #1: our language is impossible to understand\n',
        'Case #2: there are twenty six factorial possibilities\n',
        'Case #3: so it is okay if you want to just give up\n',
    ]

    result = do(cStringIO.StringIO(
        '3\n'
        'ejp mysljylc kd kxveddknmc re jsicpdrysi\n'
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n'
        'de kr kd eoya kw aej tysr re ujdr lkgc jv\n'
    ))

    print '\n'.join(result)
    assert expected == result, expected

if __name__ == "__main__":
    #test()
    print ''.join(do())
