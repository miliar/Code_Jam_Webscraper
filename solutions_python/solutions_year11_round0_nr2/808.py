import sys, re
class Robot:
    def __init__(self):
        self.position=1
        self.done = False
    def walkForward(self):
        self.position+=1
    def walkBackward(self):
        self.position-=1
    def getPosition(self):
        return self.position
    def nowDone(self):
        self.done = True
    def isDone(self):
        return self.done

p = sys.stdin
rowcount = 0
tot_cases = None
cases = []
for row in p:
    if rowcount==0:
        tot_cases = row
    else:
        cases.append(row)
    rowcount+=1

answers = []
for case in cases:
    case = case.split()
    combining = case[1:1+int(case[0])]
    opposed =case[2+int(case[0]):-2]
    test = case[-1]

    comb = {}
    opp = set()
    for item in combining:
        comb[item[:-1]] = item[-1]
        comb[item[1]+item[0]] = item[-1]
    for item in opposed:
        pat1 = re.compile('%s.*%s' %(item[0], item[1]))
        pat2 = re.compile('%s.*%s' %(item[1], item[0]))
        opp.add(pat1)
        opp.add(pat2)

    els = [test[0]]
    count = 1
    for i in range(1,len(test)):
        if not len(els)==0:
            pot = els[-1]+test[i]
        else:
            pot = test[i]
        els.append(test[i])    
        if pot in comb:
            del els[-1]
            els[-1:] = comb[pot]
        else:
            for pat in opp:
                if re.search(pat, ''.join(els)):
                    els = []
                    count = 1


    answers.append( els)

case = 1
for answer in answers:
    st = 'Case #%d: '%case+'['+', '.join(answer)+']'
    sys.stdout.write(st+'\n')
    case+=1
        








