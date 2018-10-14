from collections import defaultdict
from pprint import pprint

with file("A-large-0.in") as inp:
    with file("A-large-0.out", "w") as outp:
        full = int(inp.readline().strip())
        for casen in xrange(full):
            rows = int(inp.readline().strip())
            wins = [[0 for x in xrange(rows)] for y in xrange(rows)]
            loses = [[0 for x in xrange(rows)] for y in xrange(rows)]
            misses = [[0 for x in xrange(rows)] for y in xrange(rows)]
            for rown in xrange(rows):
                line = inp.readline()
                for coln in xrange(rows):
                    if line[coln] == "1":
                        wins[rown][coln] += 1
                    elif line[coln] == "0":
                        loses[rown][coln] += 1
                    else:
                        misses[rown][coln] += 1
            wps = [0.0 for x in xrange(rows)]
            owps = [0.0 for x in xrange(rows)]
            oowps = [0.0 for x in xrange(rows)]
            for team in xrange(rows):
                twins = float(sum(wins[team]))
                tloses = float(sum(loses[team]))
                if tloses != 0:
                    wps[team] = twins / (tloses + twins)
                else:
                    wps[team] = 1
            for team in xrange(rows):
                twpsum = 0.0
                for team1 in xrange(rows):
                    if team1 == team or misses[team1][team] > 0:
                        continue
                    twins = 0.0
                    tloses = 0.0
                    for team2 in xrange(rows):
                        if team2 == team:
                            continue
                        twins += wins[team1][team2]
                        tloses += loses[team1][team2]
                    if tloses > 0:
                        twpsum += twins / (twins + tloses)
                    else:
                        twpsum += 1
                owps[team] = twpsum / (rows - sum(misses[team]))
            for team in xrange(rows):
                owpssum = 0.0
                for team2 in xrange(rows):
                    if misses[team][team2] > 0:
                        continue
                    owpssum += owps[team2]
                oowps[team] = owpssum / (rows - sum(misses[team]))
            rpi = [0.25 * wps[t] + 0.5 * owps[t] + 0.25 * oowps[t]
                   for t in xrange(rows)]
            outp.write("Case #%s:\n" % (casen + 1))
            for t in rpi:
                outp.write("%s\n" % t)

