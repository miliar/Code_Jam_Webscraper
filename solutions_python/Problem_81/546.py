#!/usr/bin/python

import sys
from pprint import pprint
from collections import deque

TAB = '   '





def calc_WP(s):
    wins = 0
    total = 0
    for r in s:
        if r == '.':
            continue
        total += 1
        wins += (1 if r == '1' else 0)
    WP = (1.0*wins)/total
    return WP

def calc_OWP(case, i):
    owp = 0
    count = 0
    for d in xrange(len(case)):
        if d == i: 
            continue
        if list(case[d][0])[i] == '.':
            continue
        mod = list(case[d][0]) 
        mod[i] = '.'
        owp += calc_WP(mod)
        count += 1
#        print TAB*3, 'owp =', owp
#    print TAB*2, 'owp =', owp, len(case)-1
    owp /= count 
    return owp

def calc_OOWP(case, i):
    oowp = 0
    count = 0
    for d in xrange(len(case)):
        if d == i: 
            continue
        if list(case[d][0])[i] == '.':
            continue
        oowp += calc_OWP(case, d) 
        count += 1
#        print TAB*3, 'owp =', owp
#    print TAB*2, 'owp =', owp, len(case)-1
    oowp /= count 
    return oowp

def solveCase(case, debug = False):
    WP = list()
    OWP = list()
    OOWP = list()
    RPI = list()
    for d in xrange(len(case)):
        if debug:
            print 'Team', d
        WP.append( calc_WP(list(case[d][0])) )
        OWP.append( calc_OWP(case, d) )        
        OOWP.append( calc_OOWP(case, d) )        
        rpi = 0.25 * WP[d] + 0.50 * OWP[d] + 0.25 * OOWP[d]
        RPI.append(rpi)
        if debug:
            print TAB, 'WP', WP[d]
            print TAB, 'OWP', OWP[d]   
            print TAB, 'OOWP', OWP[d]
            print TAB, 'RPI', RPI[d]
        print rpi
    return RPI
            

def main(debug = False):
    if len(sys.argv) < 2:
        print 'no input file given!'
        return
    
    fin = open(sys.argv[1])
    T = fin.readline() 
    T = int(T)

    result = list()

    for c in xrange(T):
        sss = "Case #%d:" % (c+1)
        print sss
        N = int(fin.readline())
        case = list()
        for d in xrange(N):
            case.append(fin.readline().split())
#        pprint(case)
        ans = solveCase(case, debug = False)
        result.append(ans)


    fin.close()
#    writeOutput(result)
                
                
def writeOutput(result):
    fout = open('magick.out', 'w')
    for c in range(0, len(result)):
        magic = formatMagic(result[c])
        line = 'Case #%d: %s' % (c+1, magic)
        print line
        fout.write(line)
        fout.write('\n')
    fout.close()

if __name__ == '__main__':
    debug = False
    main(debug)
    
