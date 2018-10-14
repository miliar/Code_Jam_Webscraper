__author__="Administrator"
__date__ ="$Sep 3, 2009 10:33:45 AM$"
import sys
import re

def parsePhase(word):
    word=word.replace(')',']')
    word=word.replace('(','[')
    return(word)

def parseInput(fn):
    l,d,n=0,0,0
    lineNum=0
    langDict=[]
    caseDict={}
    case=1
    for line in open(fn).read().split('\n'):
        lineNum+=1
        if lineNum==1:
            l,d,n=[int(i) for i in line.split()]
        elif lineNum<=d+1:
            langDict.append(line)
        else:
            if len(line)<1:
                continue
            caseDict[case]=parsePhase(line)
            case+=1
    print 'Parse input finished!'
    return(caseDict,langDict)

def formatOutput(d,fn):
    keyList=d.keys()
    keyList.sort()
    f=open(fn,'w')
    for key in keyList:
        f.write('Case #'+str(key)+':'+' '+str(d[key])+'\n')
    f.close()
    print 'write outpu finished!'
        
if __name__ == "__main__":
    fn=sys.argv[1]
    caseResult={}
    caseDict,langDict=parseInput(fn)
    print caseDict,langDict
    for caseID,phase in caseDict.iteritems():
        count=0
        re_phase=re.compile(phase)
        for ld in langDict:
            if re_phase.match(ld):
                count+=1
        caseResult[caseID]=count
    formatOutput(caseResult,fn+'.out')
    