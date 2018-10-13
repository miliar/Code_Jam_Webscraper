import sys

def solve(input):
    T = int(input.readline())
    for t in xrange(1, T+1):
        N = int(input.readline())
        teams = []
        wplist = []
        owplist = []
        oowplist = []
        for n in xrange(N):
            schedule = input.readline().strip()
            wins = schedule.count('1')
            loses = schedule.count('0')
            teams.append(schedule)
            wplist.append(float(wins) / (wins + loses))
        for i in xrange(N):
            owp = 0
            opcount = 0
            for j in xrange(N):
                if teams[i][j] != '.':
                    opwin = teams[j].count('1')
                    oplose = teams[j].count('0')
                    if teams[j][i] == '1':
                        opwin -= 1
                    else:
                        oplose -= 1
                    owp += float(opwin) / (opwin + oplose)
                    opcount += 1 
            owplist.append(float(owp) / opcount)
        for i in xrange(N):
            oowp = 0
            oopcount = 0
            for j in xrange(N):
                if teams[i][j] != '.':
                    oowp += owplist[j]
                    oopcount += 1 
            oowplist.append(float(oowp) / oopcount)
        print "Case #%d:" % t
        for n in xrange(N):
            print RPI(wplist[n], owplist[n], oowplist[n])

def RPI(wp, owp, oowp):
    return 0.25 * wp + 0.50 * owp + 0.25 * oowp

if __name__ == '__main__':
    solve(sys.stdin)
