import sys
import re

sys.stdin.readline()
case = 0

while True:
    try:
        line = sys.stdin.readline()
    except:
        break
    teams = int(line)
    games = [0 for x in range(1,teams+1)]

    for i in range(1,teams+1):
        games[i-1] = sys.stdin.readline()
    wps = [0.0 for x in range(1,teams+1)]
    nops = [0 for x in range(1,teams+1)]

    for i in range(1,teams+1):
        wins = 0.
        losses = 0.
        for j in range(1,teams+1):
            if games[i-1][j-1] == '1':
                nops[i-1] += 1
                wins+=1
            if games[i-1][j-1] == '0':
                nops[i-1] += 1
                losses+=1
        if nops[i-1] > 0:
            wps[i-1] = wins / nops[i-1]
        else:
            wps[i-1] = 0.

    owp = [0. for x in range(1,teams+1)]
    for t in range(1,teams+1):
        ops = 0
        ps = 0.
        for i in range(1,teams+1):
            if i == t: continue
            if games[i-1][t-1] == '1':
                ops += 1
                if nops[i-1] > 1:
                    ps += ((wps[i-1]*nops[i-1])-1)/(nops[i-1]-1)
            if games[i-1][t-1] == '0':
                ops += 1
                if nops[i-1] > 1:
                    ps += ((wps[i-1]*nops[i-1]))/(nops[i-1]-1)
        owp[t-1] = 0.
        if ops > 0:
            owp[t-1] = ps/ops

    oowp = [0. for x in range(1,teams+1)]
    for t in range(1,teams+1):
        ops = 0.
        ps = 0.
        for i in range(1,teams+1):
            if i == t: continue
            if games[i-1][t-1] == '.':
                continue
            ops += 1
            ps += owp[i-1]
        if nops[t-1] > 0:
            oowp[t-1] += ps/nops[t-1]
    
    case = case + 1
    print "Case #%d:" % ( case)
    for t in range(1,teams+1):
        print "%f" % ( .25 * wps[t-1] + .5 * owp[t-1] + .25 * oowp[t-1])

