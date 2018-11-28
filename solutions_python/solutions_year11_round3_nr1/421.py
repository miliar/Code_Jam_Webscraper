#!/usr/bin/env python
from __future__ import division
import cStringIO
import fileinput


def run(infile=None):
    if infile is None:
        infile = fileinput.input()

    def get_lines(n):
        lines = list()
        for i in xrange(n):
            lines.append(infile.readline())
        return lines

    def solve(r, c, chars):
        l = list()
        for line in chars:
            line = list(line.strip())
            if line.count('#') % 2 == 1:
                return '\nImpossible'
            for i, cc in enumerate(line):
                if cc == ".":
                    continue
                try:
                    nc = line[i+1]
                except IndexError:
                    continue
                if cc == '#' and nc == '#':
                    line[i] = '/'
                    line[i+1] = '\\'
            l.append(line)

        toggled = set()

        for i, line in enumerate(l):
            for j, cc in enumerate(line):
                if cc == '/' and (i,j) not in toggled:
                    try:
                        next_line = l[i+1]
                        if line[j+1] == '\\' and next_line[j] == '/' and next_line[j+1] == '\\':
                            next_line[j] = '\\'
                            next_line[j+1] = '/'
                            toggled.add((i+1,j))
                            toggled.add((i+1,j+1))
                    except IndexError:
                        return '\nImpossible'

        ret = list()
        for line in l:
            ret.append(''.join(line))
            
        return '\n%s' % '\n'.join(ret)

    try:
        cases = int(infile.readline())
    except ValueError:
        print 'Error: Test case count not found'
        return []
    case_results = list()
    for case in xrange(cases):
        r, c = map(int, get_lines(1)[0].strip().split(' '))
        chars = get_lines(r)
        case_results.append('Case #%d:%s' % (case+1, 
                    solve(r, c, chars)))
    return case_results

def test():
    expected = [
        'Case #1:\n'
        'Impossible\n',
        'Case #2:\n'
        '.\n',
        'Case #3:\n'
        './\..\n'
        '.\//\\\n'
        './\\\\/\n'
        '.\\/..\n' 
    ]

    result = run(cStringIO.StringIO(
        '3\n'
        '2 3\n'
        '###\n'
        '###\n'
        '1 1\n'
        '.\n'
        '4 5\n'
        '.##..\n'
        '.####\n'
        '.####\n'
        '.##.'
    ))

    print '\n'.join(result)
    assert expected == result, expected

if __name__ == "__main__":
    print '\n'.join(run())
    #test()
