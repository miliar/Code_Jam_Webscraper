import time
from math import floor

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

##############################################################

def probA(filename,outputname):
    T,Cases = splitInput(filename)
    allRet = ''
    t1 = time.clock()
    for k in range(T):
        case = str2num(Cases.pop(0))
        r = case[0]
        t = case[1]
        ret = solver(r,t)
        print ret
        allRet += organiseOutputs(k+1,ret)
    t2 = time.clock()
    print t2-t1
    outputResult(outputname,allRet[0:-1],typ = '.in')




def solver(r,t):
    s = 1
    pi =  1.0
    cv = 1/pi
    r1 = r
    v1 = 0
    ct = 0
    #print r,t
    
    a = 2
    b = a+2*r-3
    c  = -t
    
    x1 = (-b+((b**2-4*a*c)**0.5))/(2*a)
    ret = int(x1)
    cp = long(a*ret**2 + b*ret)
    if cp <= t: return ret
    else: return ret-1
    

            
        
    








#########################################################
    
small = 'A-small-attempt0.in'
large = 'A-large-attempt0.in'
test = 'test.txt'
smallOut = 'resultA1'
largeOut = 'resultA2'
testOut = 'testResult'

filename =small
outputname = smallOut

probA(filename,outputname)
            
        
    
    
