# -*- coding: utf-8 -*-
"""
Created on Sat May 07 18:45:52 2011

@author: Shahar
"""



def D(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        CaseN =  int(fin.readline())
        Case = map(int, fin.readline().rstrip('\n').split(' '))
        CaseTotal = 0
        for i in xrange(len(Case)) :
            if Case[i] != i+1 :
                CaseTotal += 1                        
        text = 'Case #' + str(iCNT+1) + ': ' + ('%.06f' % CaseTotal)
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #D(sys.argv[1]);
    #D('..\\test\\D-test.in');
    #D('..\\test\\D-small-attempt0.in');
    #D('..\\test\\D-small-attempt1.in');
    D('..\\test\\D-large.in');
