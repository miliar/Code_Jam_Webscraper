from formatFile import *

cases = formatFile('Magicka.txt', 1, True)
answers = []
v = 1
for case in cases:
    print case, v
    v += 1
    case = case[0].split()

    combo = []

    #Create Combinations
    combNum = int(case.pop(0))
    comblist = []
    combs = {}
    for i in xrange(combNum):
        comblist.append(case.pop(0))
    for comb in comblist:
        combs[comb[:2]] = comb[-1]
        combs[comb[:2][::-1]] = comb[-1]
    #print combs

    #Create Oppositions
    oppNum = int(case.pop(0))
    opps = []
    for i in xrange(oppNum):
        opp = case.pop(0)
        opps.append(opp)
    #print opps

    #Create Elements
    eleNum = case.pop(0)
    eleString = case.pop(0)
    eles = []
    for ele in eleString:
        eles.append(ele)
    #print eles

    for i in xrange(len(eles)):
        combo.append(eles.pop(0))
        if len(combo) >= 2:
            lastTwo = combo[-1] + combo[-2]
            if lastTwo in combs.keys():
                combo = combo[:-2]
                combo.append(combs[lastTwo])
                
        if len(combo) >= 2:
            lastOne = combo[-1]
            for opp in opps:
                if lastOne in opp:
                    opp = opp.replace(lastOne, '')
                    if opp in combo:
                        combo = []

    print combo        
    answers.append(combo)

createAnswer(answers, 'Magicka Answers.txt')
print 'Done'

filelist = []

for line in open('Magicka Answers.txt', 'rU'):
    filelist.append(line.replace('\'',''))

print filelist

open('Magicka Answers.txt', 'w').write('')

for thing in filelist:
    open('Magicka Answers.txt', 'a').write(thing)
    
