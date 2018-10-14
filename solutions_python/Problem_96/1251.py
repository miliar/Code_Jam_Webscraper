filein = open('B-small-attempt0.in')
fileout = open('output2.txt', 'w')

class Scores:
    def __init__(self, _total):
        self.total = _total
        self.first = 0
        self.second = 0
        self.third = 0
        self.state = ''
    
    def getValues(self):
        return [self.first, self.second, self.third]
    def getTotal(self):
        return self.total
    def getState(self):
        return self.state
    def getMax(self):
        return self.third
    def checkValue(self, value):
        if self.first >= value or self.second >= value or self.third >= value:
            return True
        return False

a = filein.readlines()
b = len(a)
for c in range(0,b):
    if c == 0:
        continue
    tempStr = ''
    tempStr += 'Case #%d: ' %(c)
    d = a[c].split()
    for n in range(0, len(d)):
        d[n] = int(d[n])
    N = d[0]
    S = d[1]
    P = d[2]
    totals = []
    for n in range(3,3+N):
        totals.append(d[n])
    ScoreBoard = []
    for n in range(0, len(totals)):
        ScoreBoard.append(Scores(totals[n]))

    for n in ScoreBoard:
        if n.total%3==0:
            n.first = n.total/3
            n.second = n.total/3
            n.third = n.total/3
            n.state = 'yes'
        if n.total%3==1:
            temp = n.total-1
            n.first = temp/3
            n.second = temp/3
            n.third = temp/3
            n.third += 1
            n.state = 'no'
        if n.total%3==2:
            temp = n.total+1
            n.first = temp/3
            n.second = temp/3
            n.third = temp/3
            n.first -= 1
            n.state = 'yes'
        if n.getMax() == 0:
            n.state = 'no'

    count = 0
    losers = []
    for n in ScoreBoard:
        losers.append(n)
    for n in losers:
        if n.getMax() >= P:
            count += 1
    S1 = 0
    
    for n in losers:
        if n.getMax() == P-1 and n.getState()=='yes':
            S1 += 1
    if S >= S1:
        count += S1
    else:
        count += S

    tempStr += '%d' %(count)
    fileout.write(tempStr)
    fileout.write('\n')

filein.close()
fileout.close()
