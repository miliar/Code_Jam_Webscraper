from itertools import combinations

#inFile = "03in_test.txt"
inFile = "03in_sm.txt"
#inFile = "01in_lg.txt"
outFile = "03out_sm.txt"


def getInput(filename, delim=' '):
    f = open(filename,"r")
    indata = list()
    for line in f:
        indata.append(line.strip().split(delim))
    return indata


def max(a,b):    
    if(a >= b): return a
    else: return b
    
def psum(c,idx):
    s = 0
    for i in idx:
        s ^= c[i]
    return s

def ssum(c, idx):
    s = 0
    for i in idx:
        s += c[i]
    return s

def test( c ):
    idx = [x for x in xrange(len(c))]
    for i in xrange(1,len(idx)):
        for sub in combinations(idx,i):
            sub1 = list(sub)
            sub2 = list(set(idx)-set(sub1))
            print sub1,sub2
            
def balPart( c ):
    '''All summing must be done by xor'''
    sean = 0
    idx = [x for x in xrange(len(c))]
    for i in xrange(1,len(idx)):
        for sub in combinations(idx, i):
            sub1 = list(sub)
            sub2 = list(set(idx)-set(sub1))
            if( psum(c,sub1) == psum(c,sub2)):
                tmp = max(ssum(c,sub1),ssum(c,sub2))
                sean = max(sean,tmp)
    return sean
                
    

inData = getInput(inFile)
outData = open(outFile,'w')

case = 1    
for i in xrange(1,len(inData),2):
    c = [int(x) for x in inData[i+1]]
    v = str(balPart(c))
    if( v == '0'): v = "NO"
    #test(c)
    print "Case #" + str(case) + ": " + v
    outData.write("Case #" + str(case) + ": " + v + "\n")
    case += 1

outData.close()
