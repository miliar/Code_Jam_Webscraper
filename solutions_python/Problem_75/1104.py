
def magick(invokes,opposed,combines):
    res = []
    for i in invokes:
#        print res, i
        if len(res)==0:
            res.append(i)
            continue
        
        topTwo = i + res[len(res)-1]
        if topTwo in combines:
            res[len(res)-1] = combines[topTwo]
            continue
        
        if i in opposed:
            if opposed[i] in res:
                res = []
                continue
        res.append(i)
    return res
            
        
sample = "1 QFT 1 QF 7 FAQFDFQ"


t = int(input())
currentArg = 0
for t_no in range(1,t+1):
    allArgs = raw_input().split(" ")
    #allArgs = sample.split(" ")
    numCombines = int(allArgs[0])
    combines = {}
    x=1
    for i in range(1,numCombines+1):        
        combines[allArgs[i][0:2]]=allArgs[i][2]
        combines[allArgs[i][1::-1]]=allArgs[i][2]
        x+=1

    numInvokes = int(allArgs[x])
    x+=1
    opposed = {}
    for i in range(x,x+numInvokes):
        opposed[allArgs[i][0]]=allArgs[i][1]
        opposed[allArgs[i][1]]=allArgs[i][0]
        x+=1

    invoke=allArgs[x+1]
    res = str(magick(invoke,opposed,combines))
    print "Case #%d: %s" % (t_no,res.translate(None,"'"))