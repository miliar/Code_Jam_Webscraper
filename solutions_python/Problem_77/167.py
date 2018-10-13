'''
@author: Peratham
'''
import copy

INPUTFILE = 'D-large.in'
OUTPUTFILE = 'D-large.out'

class cmpCount:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1

def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = []
    param.append(P)
    input = []
    
    num_n = []
    text = file.readlines()
    pile = False
    for line in text:
        if pile == False:
            num_n.append(line)
            pile = True
        else:
            tmp = line.split()
            input.append(tmp)
            pile = False
    param.append(num_n)
    
    file.close()
    del file
    
    inputt = []
    for i in input:
        inputtmp = []
        for ii in i:
            inputtmp.append(int(ii))
        inputt.append(inputtmp)
    return [param, inputt]
    
def solve(param, input):
    ans = []
    for iput in input:
        ans.append(numMisplaced(iput))
    return ans

def numMisplaced(iiput):
    siiput = copy.copy(iiput)
    siiput.sort()
    cnt = 0
    for i in xrange(len(siiput)):
        if siiput[i] != iiput[i]:
            cnt += 1
    return cnt

def numSwapBSort(iiput):
    nswap = 0
    iput = copy.copy(iiput)
    leniput = len(iput)
    for j in xrange(leniput):
        for i in xrange(leniput - 1):
            if iput[i] > iput[i + 1]:
                tmp = iput[i]
                iput[i] = iput[i + 1] 
                iput[i + 1] = tmp
                nswap += 1
    print iput
    return nswap

def numSwapMSort(iiput):
    nswap = cmpCount()
    iput = copy.copy(iiput)
    leniput = len(iput)
    nswap = Msort(iput,nswap)
    
    return nswap.count

def Msort(iput,nswap):
    if len(iput) < 2:
        return iput
    hliput = len(iput)/2
    if len(iput) > 2:
        a = Msort(iput[:hliput],nswap)
        b = Msort(iput[hliput:],nswap)
        c = merge(a,b,nswap)
    return nswap
        
def merge(a,b,nswap):
    ans = []
    while len(a) > 0 and len(b) > 0:
        if a[-1] > b[-1]:
            nswap()
            ans.append(a.pop())
        else:
            nswap()
            ans.append(b.pop())
    return ans
    
def numSwapISort(iiput):
    nswap = 0
    iput = copy.copy(iiput)
    leniput = len(iput)
    for i in xrange(leniput):
        mini = min(iput[i:])
        idx_mini = iput.index(mini)
        if mini != iput[i]:
            tmp = iput[i]
            iput[i] = mini
            iput[idx_mini] = tmp
            nswap += 1
    return nswap

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    file.write("Case #1: %d\n" % ans[0])
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        file.write("Case #%d: %d\n" % ((i + 2), ans[(i + 1)]))
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
