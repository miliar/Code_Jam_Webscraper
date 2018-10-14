#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rluo
#
# Created:     12/04/2013
# Copyright:   (c) rluo 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def solve(inputfile,outputfile):
    inFile = file(inputfile,'r')
    outFile = open(outputfile,'w')
    cnt = 0;
    firstline = True
    caseLine = []
    for line in inFile.readlines():
        line = line.strip()
##        print line
        if firstline == True:
            firstline = False
            cases =int(line)
        elif len(line) >0:
            caseLine.append(line)
            if len(caseLine) == 4:
                print "Case #%d:"%(cnt+1),
                cnt+=1
                outputResult(caseLine)
                caseLine = []

def outputResult(caseLine):

    for line in caseLine:
        dicc = {'X':0,'O':0,'T':0,'.':0}
        for chr in line.strip():
##            print chr
            dicc[chr]=dicc[chr]+1
        result = makeJudgement(dicc)
        if result:
            return

    for i in range(4):
        dicc = {'X':0,'O':0,'T':0,'.':0}
        for j in range(4):
##        print "??",caseLine[i][i]
            dicc[caseLine[j][i]]+=1

        result = makeJudgement(dicc)
        if result:
            return

    dicc = {'X':0,'O':0,'T':0,'.':0}
    for i in range(4):
        dicc[caseLine[i][i]]+=1
    result = makeJudgement(dicc)
    if result:
        return

    dicc = {'X':0,'O':0,'T':0,'.':0}
    for i in range(4):
        dicc[caseLine[i][3-i]]+=1
    result = makeJudgement(dicc)
    if result:
        return

    for i in range(4):
        if "." in caseLine[i]:
            print "Game has not completed"
            return


    print "Draw"
    return



def makeJudgement(dicc):
        if dicc['X']+dicc['T'] == 4:
            print "X won"
            return True
        elif dicc['O']+dicc['T'] == 4:
            print "O won"
            return True
        return False



if __name__ == '__main__':
    inputfile="C:\\dev\\q1\\A-small-attempt0.in"
    outputfile="C:\\dev\\q1\\A-small-attempt0.out"
    solve(inputfile,outputfile)
