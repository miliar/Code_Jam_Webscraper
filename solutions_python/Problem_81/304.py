'''
Created on 21 mai 2011

@author: nicolas
'''

from __future__ import division
import sys

def solve(n, teams):
    #print teams
    
    WP = []
    wins = lambda c: c=='1'
    losses = lambda c: c=='0'
    
    nwins = []
    nlosses = []
    
    for i, t in enumerate(teams):
        nwins.append(len(filter(wins, t)))
        nlosses.append(len(filter(losses, t)))
        twp = nwins[i] / (nwins[i] + nlosses[i])
        WP.append(twp)
        
    #print WP
    
    OWP = []
    nops = []
    
    for t in teams:
        towp = 0.0
        tops = 0
        for i in range(len(t)):
            if t[i] != '.':
                tops += 1
                w = nwins[i] - (1-int(t[i]))
                l = nlosses[i] - int(t[i])
                towp += w / (w + l)
        towp /= tops
        OWP.append(towp)
        nops.append(tops)
        
    #print OWP
    
    OOWP = []
    
    for j, t in enumerate(teams):
        toowp = 0.0
        for i in range(len(t)):
            if t[i] != '.':
                toowp += OWP[i]
        toowp /= nops[j]
        OOWP.append(toowp)
    
    #print OOWP
    
    RPI = []
    for i in range(len(teams)):
        RPI.append(0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i])
        
    #print RPI
    
    print 'Case #{}:'.format(n)
    for v in RPI:
        print v
    


if __name__ == '__main__':
    filepath = sys.argv[1]
    file = open(filepath)
    
    T = int(file.readline().strip())
    
    for t in range(T):
        N = int(file.readline().strip())
        teams = []
        for n in range(N):
            teams.append(file.readline().strip())
        solve(t+1, teams)
    
    
        