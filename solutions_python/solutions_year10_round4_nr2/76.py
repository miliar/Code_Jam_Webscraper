def makeArray(dimension, initVal):
    temp = [initVal] * dimension[len(dimension)-1]
    for i in xrange(len(dimension)-2, -1, -1):
        temp = [temp] * dimension[i]
    return temp

def solve(fin, fout, caseNum):
    p = int(fin.readline().strip())
    nt = pow(2, p)
    m = map(int, fin.readline().strip().split(' '))
    q = makeArray([nt], 0)
    s = []
    n = []
    for i in xrange(p):
        temp = map(int, fin.readline().strip().split(' '))
        s.append(makeArray([len(temp)], False))
        n.append(temp)
    r = 1
    count = 0
    '''
    ni = round
    nj = position / pow(2, ni + 1)
    mS = nj * pow(2, ni + 1)
    mE = ms + pow(2, ni + 1)
    '''
    money = []
    for i in xrange(nt):
        money.append([])
        for j in xrange(p):
            ni = j
            nj = i / pow(2, ni + 1)
            #print i, j, ni, nj, n[ni][nj]
            money[i].append([n[ni][nj], ni, nj])
    #print money
    
    for i in xrange(min(m), max(m) + 1):
        for j in xrange(nt):
            if m[j] == i:
                while q[j] < p - m[j]:
                    minCost = money[j][0][0]
                    minIndex = 0
                    for k in xrange(len(money[j])):
                        if money[j][k][0] <= minCost:
                            minCost = money[j][k][0]
                            ni = money[j][k][1]
                            nj = money[j][k][2]
                            minIndex = k
                    if not s[ni][nj]:
                        #print ni, nj, n[ni][nj]
                        count += n[ni][nj]
                        s[ni][nj] = True
                        mS = nj * pow(2, ni+1)
                        mE = mS + pow(2, ni+1)
                        #print mS, mE
                        for l in xrange(mS, mE):
                            q[l] += 1
                    money[j].remove(money[j][minIndex])
    print count
    fout.write("Case #%d: %d\n" % (caseNum, count))

import sys
problem = sys.argv[0][0]
filename = sys.argv[1]
fileIn = '%s-%s.in' % (problem, filename)
fileOut = '%s-%s.out' % (problem, filename)
fin = open(fileIn, 'r')
fout = open(fileOut, 'w')
t = int(fin.readline().strip())
for i in xrange(1, t + 1):
    solve(fin, fout, i)
fin.close()
fout.close()