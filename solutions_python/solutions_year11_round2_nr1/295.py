#
# Google Code Jam 2011
# Roaund 1B: A. RPI
# submission by EnTerr
#

'''

Input 
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.

Output 
 
Case #1:
0.5
0.5
0.5
Case #2:
0.645833333333
0.368055555556
0.604166666667
0.395833333333

'''

import sys
import psyco
psyco.full()

inf = open(sys.argv[1])
def input(): return inf.readline().strip()

def avg(scores):
    num = 0.
    denum = 0.
    #print scores
    for v in scores:
        num += v[0]
        denum += v[1]
    return num / denum


def rpi(games):
    global guest
    global home
    global P
    guest = {}
    home = {}
    P = {}
    for x,y,_ in games:
        guest[x] = []
        guest[y] = []
        home[x] = []
        home[y] = []
        
    for x,y,win in games:
        f = 14 - 8 * win
        guest[x].append( (win*f, f, y) )
        guest[y].append( (f - win*f, f, x) )
        home[x].append( (win, 1, y) )
        home[y].append( (1-win, 1, x) )
        
    for t in home:
        P[t] = avg([ (avg([(x,y) for x,y,z in home[o] if z!=t]), 2)
                      for i,j,o in home[t]
                    ])
    #print 'home', home
    #print 'guest', guest
    for t in home:
        home[t] = avg( [(P[o],2) for x,y,o in home[t]]) 
        home[t] += avg( guest[t] )/4                     
        home[t] += P[t]
        
    return home


for caseNo in range(1, int(input())+1):
    print >>sys.stderr, caseNo
    print 'Case #%d:' % caseNo
    sco = []
    for i in range(int(input())):
        s = input()
        for j in range(len(s)):
            if s[j] in '01':
                sco.append( [i,j, int(s[j])] )
    r = rpi(sco)
    for i in range(len(r)):
        print r[i]

