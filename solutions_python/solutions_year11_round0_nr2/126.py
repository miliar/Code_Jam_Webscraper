# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:49:56 2011

@author: Shahar
"""



def B(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        Case = fin.readline().rstrip('\n').split(' ')
        nCombined = int(Case[0])
        CombinePairs = Case[1:nCombined+1]
        nOpposed = int(Case[nCombined+1])
        OpposePairs = Case[nCombined+2:nCombined+nOpposed+2]
        Invoked = Case[nCombined+nOpposed+3]
        Combine = {}
        Oppose = {}
        for CombinePair in CombinePairs :
            Combine[CombinePair[0:2]] = CombinePair[2]
            Combine[CombinePair[0:2][::-1]] = CombinePair[2]
        for OpposePair in OpposePairs :
            if not OpposePair[0] in Oppose :
                Oppose[OpposePair[0]] = []
            if not OpposePair[1] in Oppose :
                Oppose[OpposePair[1]] = []
            Oppose[OpposePair[0]].append(OpposePair[1])
            Oppose[OpposePair[1]].append(OpposePair[0])
        FinalList = ['*']
        for Element in Invoked :
            LastPair = FinalList[-1] + Element
            if LastPair in Combine :
                FinalList[-1] = Combine[LastPair]
            else:
                Opposing = False
                if Element in Oppose :
                    CurrOpposed = Oppose[Element]
                    for OpposedElement in CurrOpposed :
                        if FinalList.count(OpposedElement) > 0 :
                            FinalList = ['*']
                            Opposing = True
                            break
                if not Opposing :
                    FinalList.append(Element)

        text = 'Case #' + str(iCNT+1) + ': ['
        if len(FinalList) > 1:
            for Element in FinalList[1:-1] :
                text += Element + ', '
            text += FinalList[-1]
        text += ']'
        
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #B(sys.argv[1]);
    #B('..\\test\\B-test.in');
    #B('..\\test\\B-small-attempt0.in');
    #B('..\\test\\B-small-attempt1.in');
    B('..\\test\\B-large.in');
