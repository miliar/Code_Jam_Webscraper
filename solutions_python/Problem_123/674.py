import time
from math import *

################# Helper Function ##########################
def splitInput(filename):
    inFile = open(filename,'r')
    inPut = inFile.read()
    inPut = inPut.split('\n')
    T = int(inPut[0])

    Cases = inPut[1:]
    emt = Cases.count('')
    for h in range(emt):
        Cases.remove('')
    inFile.close()

    return (T,Cases)

def outputResult(name,stuffs,typ = '.in'):
    output = open(name+typ,'w')
    output.write(stuffs)
    output.close()
    return

def organiseOutputs(caseNumber,singleOutput):
    
    return 'Case #%d:' % (caseNumber) + " "+str(singleOutput)+'\n'

def addEachToElement(initial,addend):
    hld = []
    ct = -1
    same = type([1,2]) == type(initial[0])
    for elm in initial:
        ct += 1
        if same:
            elm.append(addend[ct])
            hld.append(elm)
        else:
            hld.append([elm,addend[ct]])
    return hld


def str2num(strg,typ = 'i'):
    alist = strg.split(' ')
    newList = []
    for item in alist:
        if item != ' ':
            
            if typ == 'i':
                newList.append(int(item))
            else:
                newList.append(float(item))
    return newList

####################### Main Code ##############################

def probA(filename,outputname):
    T,Cases = splitInput(filename)
    allRet = ''
    t1 = time.clock()
    for k in range(T):
        AN = str2num(Cases.pop(0))
        A = AN[0]
        N = AN[1]
        motes = str2num(Cases.pop(0))
        ret = solver(N,A,motes)
        allRet += organiseOutputs(k+1,ret)
    t2 = time.clock()
    print t2-t1
    outputResult(outputname,allRet[0:-1],typ = '.in')




def solver(N,A,motes):
    motes.sort()
    moteQueue = [motes[:]]
    AQueue = [A]
    ctQueue = [0]
    while moteQueue:
        mote = moteQueue.pop(0)
        ct = ctQueue.pop(0)
        a = AQueue.pop(0)
        st = True
        while st and mote:
            st = False
            f = mote[0]
            if a>f:
                a += f
                mote = mote[1:]
                st = True
        if len(mote) == 0: return ct
        if len(mote) == 1: return ct+1
        if min(mote) == max(mote) and mote[0] == 1: return len(mote) + ct
        moteQueue.append([a-1]+mote)
        moteQueue.append(mote[0:-1])
        ctQueue.append(ct+1)
        ctQueue.append(ct+1)
        AQueue.append(a)
        AQueue.append(a)
    print 'yyyyeeeeeeeeeee'
    return 'Yessssssssssss'
        



####################### Run Code #############################
    
small = 'A-small-attempt4.in'
large = 'A-large-attempt0.in'
test = 'test.txt'
smallOut = 'resultA4'
largeOut = 'resultA3'
testOut = 'testResult'

filename =small
outputname = smallOut

probA(filename,outputname)
            
        
    
    
