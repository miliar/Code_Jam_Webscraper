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
        Case = fin.readline().rstrip('\n').split(' ')
        SeqSteps = [0]
        PrevRobot = 'N'
        Pos = {'O':1, 'B':1}
        for iStep in xrange(int(Case[0])) :
            Robot = Case[2*iStep+1]
            Button = int(Case[2*iStep+2])
            CurrStep = abs(Pos[Robot]-Button)+1
            if PrevRobot != Robot : 
                SeqSteps.append(0)
                PrevRobot = Robot
                SeqSteps[-1] += max(CurrStep - SeqSteps[-2], 1)
            else :
                SeqSteps[-1] += CurrStep
            Pos[Robot] = Button
        TotalSteps = sum(SeqSteps)
            
        text = 'Case #' + str(iCNT+1) + ': ' + str(TotalSteps)
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #A(sys.argv[1]);
    #A('..\\test\\A-test.in');
    #A('..\\test\\A-small-attempt0.in');
    #A('..\\test\\A-small-attempt1.in');
    A('..\\test\\A-large.in');
