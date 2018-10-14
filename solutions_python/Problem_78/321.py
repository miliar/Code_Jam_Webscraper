#!/usr/bin/env python
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

    def solve(l):
        n, pd, pg = l
        if (pg == 100 and pd != 100) or (pg == 0 and pd != 0):
            return 'Broken'
        if (pg == 100 and pd == 100) or (pg == 0 and pd == 0):
            return 'Possible'

        # pd = wd / d
        # pg = wg / g
        # g => d

        # if pd < pg -> wg > wd and g > d
        #   prove: wg <= wd
        # if pd > pg -> wd < wg and g > d 
        #   prove: wd >= wg

        pd = float(pd) / 100
        pg = float(pg) / 100
        #print "*** [DEBUG] ", l
        for d in xrange(1,n+1):
            wd = d * pd
            if wd % 1 != 0:
                continue
            o = 0
            while True:
                g = wd + o
                wg = g * pg
                o += 1
                if wg % 1 != 0:
                    continue

                #print "*** [DEBUG] d:", pd, wd, d
                #print "*** [DEBUG] g:", pg, wg, g

                if pd < pg and wg > wd:
                    return 'Possible'
                if pd > pg and wd < wg:
                    return 'Possible'

                if pd < pg and wd <= wg:
                    #print "*** [DEBUG] d:", pd, wd, d
                    #print "*** [DEBUG] g:", pg, wg, g
                    break
                if pd > pg and wd > wg:
                    #print "*** [DEBUG] d:", pd, wd, d
                    #print "*** [DEBUG] g:", pg, wg, g
                    break
                
        return 'Broken'

    try:
        cases = int(infile.readline())
    except ValueError:
        print 'Error: Test case count not found'
        return []
    case_results = list()
    for case in xrange(cases):
        lines = get_lines(1)
        case_results.append('Case #%d: %s' % (case+1, 
                    solve(map(int, lines[0].split(' ')))))
    return case_results

def test():
    expected = [
        'Case #1: Possible',
        'Case #2: Broken',
        'Case #3: Possible',
        'Case #4: Broken',
        'Case #5: Broken',
        'Case #6: Possible',
        'Case #7: Possible',
        'Case #8: Possible',
    ]

    result = run(cStringIO.StringIO(
        '8\n'
        '1 100 50\n'
        '10 10 100\n'
        '9 80 56\n'
        '10 96 100\n'
        '7 16 23\n'
        '6 100 100\n'
        '10 0 0\n'
        '10 30 51\n'
    ))

    print '\n'.join(result)
    assert expected == result, expected

if __name__ == "__main__":
    print '\n'.join(run())
    #test()
