f = open('D-large.in','r')
text = f.read()
text = text.replace('\r','').strip()
lines = text.split('\n')
count = int(lines[0])
cases = lines[1:]
caseIdx = 1

for index in xrange(3,len(cases)+1,3):
    case = cases[index-3:index]
    num = int(case[0])
    naomi = case[1].strip().split(' ')
    ken = case[2].strip().split(' ')
    naomi = map(float,naomi)
    ken = map(float,ken)
    ken.sort()
    naomi.sort()

    kenDeceit = ken[:]
    copy = ken[:]
    
    score = 0
    deceit = []
    for n in naomi:
        smallIdx = [i for i,v in enumerate(kenDeceit) if v < n]
        largeIdx = [i for i,v in enumerate(ken) if v > n]

        if len(largeIdx) > 0:
            del ken[largeIdx[0]]
        else:
            del ken[0]
            score += 1

        if len(smallIdx) > 0:
            deceit.append(kenDeceit[-1]+0.000001)
            del kenDeceit[0]
        else:
            deceit.append(kenDeceit[-1]-0.000001)
            del kenDeceit[-1]


    ken = copy[:]
    deceitScore = 0

    for n in deceit:
        idx = [i for i,v in enumerate(ken) if v > n]
        if len(idx) > 0:
            del ken[idx[0]]
        else:
            del ken[0]
            deceitScore += 1

    print 'Case #'+str(caseIdx)+': '+str(deceitScore)+' '+str(score)
    caseIdx += 1
