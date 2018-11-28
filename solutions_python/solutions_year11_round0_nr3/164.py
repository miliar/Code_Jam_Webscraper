'''
@author: Peratham
'''
import copy

INPUTFILE = 'C-large.in'
OUTPUTFILE = 'C-large.out'
         

def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = []
    param.append(P)
    input = []
    
    num_candy = []
    text = file.readlines()
    pile = False
    for line in text:
        if pile == False:
            num_candy.append(line)
            pile = True
        else:
            tmp = line.split()
            input.append(tmp)
            pile = False
    param.append(num_candy)
    
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
    cnt = 1
    for iput in input:
        print cnt
        cnt += 1
        allpile = generatePiles(iput)
        if allpile == []:
            ans.append(-1)
        else:
            ans.append(max(allpile))
    return ans

def generatePiles(iput):
    allpile = []
    iiput = copy.copy(iput)
    iiput.sort()
    if addByPatrickAll(iiput):
        allpile.append(addBySeanAll(iiput[1:]))
        
    return allpile

def addBySeanAll(list):
    sall = 0
    for i in list:
        sall += i
    return sall

def addBySean(lp, rp):
    slp = 0
    for i in lp:
        slp += i
    srp = 0
    for i in rp:
        srp += i
    return max([slp, srp])

def addByPatrickAll(list):
    sall = 0
    for i in list:
        sall ^= i
    return sall == 0

def addByPatrick(lp, rp):
    if len(lp) < 1 or len(rp) < 1:
        return False
    slp = 0
    for i in lp:
        slp ^= i
    srp = 0
    for i in rp:
        srp ^= i
    return slp == srp

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    value = ans[0]
    if value < 0:
        file.write("Case #1: NO\n")
    else:
        file.write("Case #1: %d\n" % ans[0])
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        value = ans[(i + 1)]
        if value < 0:
            file.write("Case #%d: NO\n" % ((i + 2)))
        else:
            file.write("Case #%d: %d\n" % ((i + 2), value))
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
