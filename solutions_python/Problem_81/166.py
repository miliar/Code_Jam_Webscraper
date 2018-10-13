# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:07:30 2011

@author: Shahar
"""


def A(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        Teams = int(fin.readline())
        Matches = []
        WP = []
        Games = []
        Wins = []
        for iT in xrange(Teams) :
            Matches.append(list(fin.readline().rstrip('\n')))
            Games.append(0.0)
            Wins.append(0.0)
            for jT in xrange(Teams) :
                if Matches[iT][jT] == '1' :
                    Wins[iT] += 1
                if Matches[iT][jT] != '.' :
                    Games[iT] += 1
            WP.append(Wins[iT] / Games[iT])
        OWP = []
        for iT in xrange(Teams) :
            OWP.append(0.0)
            nOWP = 0
            for jT in xrange(Teams) :
                if Matches[jT][iT] == '0' :
                    OWP[iT] += (Wins[jT])/(Games[jT]-1)
                    nOWP += 1
                elif Matches[jT][iT] == '1' :
                    OWP[iT] += (Wins[jT]-1)/(Games[jT]-1)
                    nOWP += 1
            OWP[iT] =OWP[iT] / nOWP
        OOWP = []
        for iT in xrange(Teams) :
            OOWP.append(0.0)
            nOOWP = 0
            for jT in xrange(Teams) :
                if Matches[jT][iT] != '.' :
                    OOWP[iT] += OWP[jT]
                    nOOWP += 1
            OOWP[iT] = OOWP[iT] / nOOWP
        text = 'Case #' + str(iCNT+1) + ': '
        print text
        fout.write(text + '\n')
        for iT in xrange(Teams) :
            RFI = 0.25 * WP[iT] + 0.50 * OWP[iT] + 0.25 * OOWP[iT]
            text = str(RFI)
            print text
            fout.write(text + '\n')

if __name__ == "__main__":
    #A(sys.argv[1]);
    #A('..\\test\\A-test.in');
    #A('..\\test\\A-small-attempt0.in');
    #A('..\\test\\A-small-attempt1.in');
    A('..\\test\\A-large.in');
