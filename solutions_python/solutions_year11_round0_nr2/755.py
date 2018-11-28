import sys
def printOut():
    raw=raw_input()
    raw=raw.split(' ')
    ncombine=int(raw[0])
    noppose=int(raw[ncombine+1])

    test = False

    combineList=raw[1:ncombine+1]
    opposeList=raw[ncombine+2:noppose+ncombine+2]

    spell=raw[noppose+ncombine+3:]

    if test is True:
        print ncombine
        print noppose
        print combineList
        print opposeList
        print spell

    spell = spell[0]

    finalSpell = []

    finalSpell.append(spell[0])


    def checkCombine(p,q):
        if ncombine is 0: return '$'
        for i in xrange(0,ncombine):
            tmpCombine=combineList[i]
            if tmpCombine[0] is p and tmpCombine[1] is q: return tmpCombine[2]
            if tmpCombine[1] is p and tmpCombine[0] is q: return tmpCombine[2]
            return '$'

    def checkOppose(tSpell):
        if noppose is 0: return False
        for i in xrange(0,noppose):
            tmpOppose=opposeList[i]
            if tmpOppose[0] in tSpell and tmpOppose[1] in tSpell:
                if tSpell.index(tmpOppose[0]) is tSpell.index(tmpOppose[1]): return False
                return True
        return False
            

    for i in xrange(1,len(spell)):
        # print "\n\nINPUT IS ",spell[i]
        if len(finalSpell)>0: test = checkCombine(finalSpell[-1:][0],spell[i])
        else: test = '$'
        if test is not '$' :
            #print "Test is: ",test
            finalSpell.pop()
            finalSpell.append(test)
        else:
            finalSpell.append(spell[i])
        if len(finalSpell)>1:
            if checkOppose(finalSpell) is True: finalSpell = []
        #print finalSpell

    def fancyPrint(lst):
        for i in xrange(0,len(lst)):
            if i is 0: sys.stdout.write(lst[i])
            #if i < (len(lst)-1): print lst[i]+',',
            else:
                sys.stdout.write(', ')
                sys.stdout.write(lst[i])

    sys.stdout.write('[')
    fancyPrint(finalSpell)
    print ']'
    #print finalSpell

sys.stdin = open("2in.txt", "r")

sys.stdout = open("2out.txt", "w")

T = input()
for i in xrange(0,T):
    print "Case #{0}:".format(i+1),
    printOut()
sys.stdout.close()
