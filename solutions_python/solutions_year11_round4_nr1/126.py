# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:07:30 2011

@author: Shahar
"""

import operator as op
from numpy import argsort
    
def A(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        Line = map(int, fin.readline().strip('\n').split(' '))
        Corridor = float(Line[0])
        WalkSpeed = float(Line[1])
        RunSpeed = float(Line[2])
        RunTime = float(Line[3])
        nWalkways = Line[4]
        
        WWLength = []
        WWSpeed = []
        WWStart = []
        WWEnd = []
        
        for iWW in xrange(nWalkways) :
            Line = map(float, fin.readline().strip('\n').split(' '))
            WWStart.append(Line[0])
            WWEnd.append(Line[1])
            WWSpeed.append(Line[2])
            WWLength.append(Line[1]-Line[0])
        
        NoWW= WWStart[0]
        for iWW in xrange(1, nWalkways) :
            NoWW +=WWStart[iWW] - WWEnd[iWW-1]
        NoWW += Corridor - WWEnd[-1]

        if NoWW > 0 :
            WWSpeed.append(0.0)
            WWLength.append(NoWW)
        
        TravelTime = 0.0
        RunTimeLeft = RunTime
        Order = argsort(WWSpeed)
        for iO in xrange(len(Order)) :
            iWW = Order[iO]
            if RunTimeLeft > 0 :
                AllRun = WWLength[iWW] / (WWSpeed[iWW]+RunSpeed)
                if RunTimeLeft >= AllRun :
                    TravelTime += AllRun
                    RunTimeLeft -= AllRun
                else :
                    DistnaceRun = RunTimeLeft*(WWSpeed[iWW]+RunSpeed)
                    WalkTime = (WWLength[iWW]-DistnaceRun) / (WWSpeed[iWW]+WalkSpeed)
                    TravelTime += RunTimeLeft + WalkTime
                    RunTimeLeft = 0
            else :
                TravelTime += WWLength[iWW] / (WWSpeed[iWW]+WalkSpeed)
        
        text = 'Case #' + str(iCNT+1) + ': ' + str(TravelTime)
        print text
        fout.write(text + '\n')


if __name__ == "__main__":
    #A(sys.argv[1]);
    #A('..\\test\\A-test.in');
    #A('..\\test\\A-small-attempt0.in');
    #A('..\\test\\A-small-attempt1.in');
    A('..\\test\\A-large.in');
