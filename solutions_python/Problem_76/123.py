# -*- coding: utf-8 -*-
"""
Created on Sat May 07 11:45:04 2011

@author: Shahar
"""

from operator import add

def C(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        nCandies = int(fin.readline())
        CandiesVals = map(int,fin.readline().rstrip('\n').split(' '))
        CandiesVals.sort()
        CandiesVals.reverse()
        binZero =list('0'*(len(bin(10**6))-2));
        allCandies = binZero
        for Candy in CandiesVals :
            allCandies =PAdd(allCandies, Candy)
        if allCandies == binZero :
            maxS = sum(CandiesVals) - min(CandiesVals)
            text = 'Case #' + str(iCNT+1) + ': ' + str(maxS)
        else :
            text = 'Case #' + str(iCNT+1) + ': NO' 
        print text
        fout.write(text + '\n')

def MaxCandies(SSum, PSum1, PSum2, CandiesVals) :
    print 'Begin', SSum, reduce(add, PSum1), reduce(add, PSum2), CandiesVals
    if (len(CandiesVals) == 0) :
        if PSum1 == PSum2 :
            return SSum
        else :
            return -1;
            
    MaxValue = -1;
    CurrCandy = CandiesVals[0]
    MaxWith = MaxCandies(SSum+CurrCandy, PAdd(PSum1,CurrCandy), \
        PSum2, CandiesVals[1:])
    MaxWithout = MaxCandies(SSum, PSum1, PAdd(PSum2,CurrCandy), CandiesVals[1:])
    MaxValue = max(MaxWith, MaxWithout)

    print 'End', SSum, reduce(add, PSum1), reduce(add, PSum2), CandiesVals, MaxValue
    return MaxValue
    
def PAdd(aa, b) :
    bbin = bin(b)[2:];
    res = aa[:]
    for i in xrange(len(bbin)) :
        if aa[-1-i] == bbin[-1-i] :
            res[-1-i] = '0'
        else :
            res[-1-i] = '1'
    return res
    
if __name__ == "__main__":
    #C(sys.argv[1]);
    #C('..\\test\\C-test.in');
    #C('..\\test\\C-small-attempt0.in');
    #C('..\\test\\C-small-attempt1.in');
    C('..\\test\\C-large.in');
