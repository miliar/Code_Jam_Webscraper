import os, sys
from math import *

def solve(sched, nteams):
    wp = []
    for i in range(0, nteams):
        s = sched[i]
        total = 0
        win   = 0
        for r in s:
           if r == '1':
               total += 1
               win += 1
           elif r == '0':
               total += 1
        wp.append(None)
        wp[i] = float(win) / float(total)

    
    owp = []
    for i in range(0, nteams):
        owp_t = 0.0
        ops = 0
        for o in range(0, nteams):
            if o != i and sched[i][o] != '.':
                total = 0
                win   = 0
                s     = sched[o]
                ops += 1
                for k in range(0, nteams):
                    if k != i:
                        r = s[k]
                        if r == '1':
                            total += 1
                            win   += 1
                        elif r == '0':
                            total += 1

                owp_t += float(win) / float(total)
        owp.append(None)
        if ops > 0:

            owp[i] = owp_t / float(ops)
        else:
            owp[i] = 0.0

        

    oowp = []
    for i in range(0, nteams):
        oowp_t = 0.0
        ops = 0
        for o in range(0, nteams):
            if o != i and sched[i][o] != '.':
                oowp_t += owp[o]
                ops += 1
        oowp.append(None)
        if ops > 0:
            oowp[i] = oowp_t / float(ops) 
        else:
            oowp[i] = 0.0

    
    results = []
    for i in range(0, nteams):
        results.append(None)
        results[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
    return results
                    

nCases = int(sys.stdin.readline())

for case in range(1, nCases + 1):
    nteams = int(sys.stdin.readline().split()[0])
    sched = []
    for i in range(0, nteams):
        sched.append(None)
        sched[i] = sys.stdin.readline().split()[0]
    print "Case #" + str(case) + ":"
    results = solve(sched, nteams)
    for r in results:
        print r
