import sys

lines = sys.stdin.readlines()
X = 1
for d in range(int(lines[0].strip())):
    N, = map( int, lines[X].strip().split() )
    schedule = map( lambda x:x.strip(), lines[X+1:X+1+N] )
    X += N+1
    print >>sys.stderr, N,schedule
    print "Case #%d:" % (d+1)

    def WP(team, trash=-1):
        team=list(team)
        if trash >= 0: team[i]='.'
        total = len(filter(lambda x:x in ('0','1'), team))
        res = len(filter(lambda x:x == '1', team)) / float(total)
        return res

    owps={}
    for i,team in enumerate(schedule):
        total=0; owps[i] = 0
        for j,v in enumerate(team):
            if v != '.':
                owps[i] += WP(schedule[j],i)
        total = len(filter(lambda x:x in ('0','1'), team))
        owps[i] /= float(total)

    for i,team in enumerate(schedule):
        OOWP = 0
        for j,v in enumerate(team):
            if v != '.':
                OOWP += owps[j]
        total = len(filter(lambda x:x in ('0','1'), team))
        OOWP /= float(total)
        RPI = 0.25 * WP(team) + 0.50 * owps[i] + 0.25 * OOWP
        print RPI
