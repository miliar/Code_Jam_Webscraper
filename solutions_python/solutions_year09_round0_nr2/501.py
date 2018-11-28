__author__="Administrator"
__date__ ="$Sep 3, 2009 10:33:45 AM$"
import sys
import re

class Ddict(dict):
    def __init__(self, default=None):
        self.default = default

    def __getitem__(self, key):
        if not self.has_key(key):
            self[key] = self.default()
        return dict.__getitem__(self, key)

def parsePhase(word):
    word=word.replace(')',']')
    word=word.replace('(','[')
    return(word)

def parseInput(fn):
    caseNum=0
    lineNum=0
    caseAltitude={}
    caseHL={}
    case=1
    flag=1
    caseEndRow=0
    for line in open(fn).read().split('\n'):
        lineNum+=1
        if lineNum==1:
            caseNum=int(line)
        else:
            words=line.split()
            if len(words)<1:
                continue
            if flag:
                caseEndRow=lineNum+int(words[0])
                caseAltitude[case]=[]
                caseHL[case]=[int(i) for i in words]
                flag=0
            elif (lineNum<caseEndRow):
                caseAltitude[case].append([int(i) for i in words])
            elif (lineNum==caseEndRow):
                caseAltitude[case].append([int(i) for i in words])
                flag=1
                case+=1

    print 'Parse input finished!'
    return(caseAltitude,caseHL)

def formatOutput(d,caseHL,fn):
    keyList=d.keys()
    keyList.sort()
    f=open(fn,'w')
    for key in keyList:
        HL=caseHL[key]
        points=d[key]
        f.write('Case #'+str(key)+':\n')
        for row in range(0,HL[0]):
            for col in range(0,HL[1]):
                f.write(points[row][col]['label']+' ')
            f.write('\n')

    f.close()
    print 'write outpu finished!'

def calOutDegree(AltitudeList,HL):
    from operator import itemgetter
    points=Ddict(dict)
    for row in range(0,HL[0]):
        for col in range(0,HL[1]):
            points[row][col]={'outStream':[],'inStream':[],'label':''}
    for row in range(0,HL[0]):
        for col in range(0,HL[1]):
            # 1,2,3,4 represent North, West, East, South
            direction={0:(row,col),1:(row-1,col),2:(row,col-1),3:(row,col+1),4:(row+1,col)}
            neighborRev=Ddict(list)
            neighborRev[AltitudeList[row][col]].append(0)
            if (row-1)>=0:
                neighborRev[AltitudeList[row-1][col]].append(1)
            if (col-1)>=0:
                neighborRev[AltitudeList[row][col-1]].append(2)
            if col+1<HL[1]:
                neighborRev[AltitudeList[row][col+1]].append(3)
            if row+1<HL[0]:
                neighborRev[AltitudeList[row+1][col]].append(4)
            neighborSink=sorted(sorted(neighborRev.items())[0][1])
            outStream=direction[neighborSink[0]]
            points[row][col]['outStream']=[outStream]
            if outStream==(row,col):
                continue
            points[outStream[0]][outStream[1]]['inStream'].append((row,col))
    return(points)

def labelPoints(points,HL):
    import string
    letters=list(string.letters)
    lettersIdx=0
    for row in range(0,HL[0]):
        for col in range(0,HL[1]):
            if len(points[row][col]['label'])>0:
                continue
            else:
                points[row][col]['label']=letters[lettersIdx]
                # get the DAG
                flag=1
                setDAG=set([(row,col)])
                lLen=len(setDAG)
                while flag:
                    for p in list(setDAG):
                        inStream=points[p[0]][p[1]]['inStream']
                        setDAG.update(inStream)
                        outStream=points[p[0]][p[1]]['outStream']
                        setDAG.update(outStream)
                    if len(setDAG)==lLen:
                        flag=0
                    lLen=len(setDAG)
                # mark the DAG the same label
#                print setDAG,letters[lettersIdx]
                for p in setDAG:
                    points[p[0]][p[1]]['label']=letters[lettersIdx]
                lettersIdx+=1
    return(points)

if __name__ == "__main__":
    fn=sys.argv[1]
    #fn='test.in'
    caseResult={}
    #1. parse imput file, get the hight of each points
    caseAltitude,caseHL=parseInput(fn)
    
    for caseID,altitudeList in caseAltitude.iteritems():
        print caseID
        points=calOutDegree(altitudeList,caseHL[caseID])
        points=labelPoints(points,caseHL[caseID])
        caseResult[caseID]=points
 
    formatOutput(caseResult,caseHL,fn+'.out')
