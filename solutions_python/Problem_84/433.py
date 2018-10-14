#!/usr/bin/env python

import re


retile = re.compile(r'\#\#')
re12 = re.compile(r'12')
re34 = re.compile(r'34')

def test_result(case):

    R, C, lines = case

    ts = []

    ts.append( retile.sub(r'12', lines[0]) )

    if ts[0].find('#') >= 0:
        return 'Impossible'

    prev = ts[0]
    
    for r in xrange(1,len(lines)):
        line = lines[r]
        for i in xrange(len(prev)):
            if prev[i:i+2] == '12':
                line = line[:i] + '34' + line[i+2:]
        if r != len(lines)-1:
            line = retile.sub(r'12', line)
        if line.find('#') >= 0:
            return 'Impossible'
        ts.append(line)
        prev = line

    return '\n'.join(re34.sub(r'\\/', re12.sub(r'/\\', t)) for t in ts)



if __name__ == "__main__":
    
    import sys

    lines = (line for line in open(sys.argv[1]).readlines())
    nl = lambda: next(lines)

    T = int(nl())

    for t in xrange(1, T + 1):

        R, C = map(int, nl().split())

        case = []
        for i in xrange(R):
            case.append( nl()[:-1] ) 


        print 'Case #%d:\n%s' % (t,  test_result( (R, C, case) )  )
