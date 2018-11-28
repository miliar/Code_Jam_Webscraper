#!/usr/bin/env python

def WP(results):
    ones  = float(results.count('1'))
    zeros = float(results.count('0'))
    return ones / (ones + zeros)


def OWP(team, case):
    oppcases = (case[t] for t in xrange(len(case)) if t != team and case[t][team] != '.')
    owps = [c[:team] + '.' + c[team+1:] for c in oppcases]
    return sum(map(WP, owps)) / len(owps)


def test_result(case):

    OWPs = []

    for t in xrange(len(case)):
        OWPs.append( OWP(t, case) )

    OOWP = []

    for t in xrange(len(case)):
        oppOWP = [OWPs[opp] for opp in xrange(len(case)) if opp != t and case[opp][t] != '.']
        OOWP.append( sum(oppOWP) / len(oppOWP) )

    return '\n'.join([''] + map(str, (0.25 * WP(case[t]) + 0.50 * OWP(t, case) + 0.25 * OOWP[t] for t in xrange(len(case)))))



if __name__ == "__main__":
    
    import sys
    import select

    try:
        try:
            data = open(sys.argv[1])
        except:
            data = sys.stdin
        if select.select([data,],[],[],0.0)[0]:
            lines = (line for line in data.readlines())
            nl = lambda: next(lines)
    except:
        sys.exit('Usage: %(file)s input-filename' % dict(file=__file__))

    T = int(nl())

    for t in xrange(1, T + 1):

        N = int(nl())

        case = []
        for i in xrange(N):
            case.append( nl()[:-1] ) 

        print 'Case #%d: %s' % (t, test_result(case))
