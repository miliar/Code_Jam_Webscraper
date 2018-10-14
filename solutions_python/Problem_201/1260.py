import math
def readNSolve():
    with open ('C-small-2-attempt0.in') as f:
        first=f.readline()
        caseNum=1
        for line in f:
            result=solve(line)
            writeOutput(caseNum,result)
            caseNum+=1
def writeOutput(caseNum,result):
    out = open('C-small-2-attempt0.out', 'a')
    out.write('Case #{}: {} {}\n'.format(caseNum, result[0],result[1]))
def getListInt(line):
    lst=[]
    line=str(line)
    for i in range(len(line)):
        lst.append(int(line[i]))
    return lst

def solve(line):
    splits=line.split(" ")
    last = getLastBlank(int(splits[1]),int(splits[0]))
    last-=1
    return (math.ceil(last/2),math.floor(last/2))
def pushAndReduce(num,freq,lst):
    exist=False
    for i in range(len(lst)):
        if (lst[i]['name']==num):
            exist=True
            lst[i]['freq']+=freq
    if(exist==False):
        lst.append({'name':num,'freq':freq})
def getLastBlank(k,n):
    mainlst=[{'name':n,'freq':1}]
    i=0
    while True:
        num=2**i
        if(k>num):
            templst=[]
            for x in range(len(mainlst)):
                currNum=mainlst[x]['name']-1
                currFreq=mainlst[x]['freq']
                pushAndReduce(math.ceil(currNum/2),currFreq,templst)
                pushAndReduce(math.floor(currNum/2), currFreq, templst)
            mainlst=templst
            k-=num
            i+=1
        else:
            return mainlst[1]['name'] if k>mainlst[0]['freq'] else mainlst[0]['name']
readNSolve()