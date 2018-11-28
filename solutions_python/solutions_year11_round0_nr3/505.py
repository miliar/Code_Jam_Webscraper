f = open('C-large.in')
x = f.readlines()
x.pop(0)


def patrick_addnumbers(x,y):
    binx = bin(x) 
    biny = bin(y)
    xcount = len(binx)-1
    ycount = len(biny)-1

    answer= ""
    while binx[xcount]!='b' and biny[ycount]!='b':
        if(binx[xcount] == biny[ycount]):
            answer = '0'+answer
        else:
            answer = '1'+answer 
        xcount-=1
        ycount-=1

    if binx[xcount]!='b':
        answer = binx[:xcount+1] + answer
    if binx[ycount]!='b':
        answer = biny[:ycount+1] + answer

    return int(answer,2)
    

def xorit(ar):
    tally = None
    for d in ar:
        if not tally:
            tally = d
        else:
            tally = tally ^ d

    return tally

def sumit(ar):
    answer = 0

    for d in ar:
        answer +=d

    return answer 
    
case = 1
while len(x):
    x.pop(0)
    candies = [int(g) for g in x[0].split()]
    candies.sort()
    candies.reverse()
    x.pop(0)
    tally = None
    answer = "NO" 
    for candy in candies:
        if not tally:  
            tally = candy
        else:
            tally = candy^tally

    if tally != 0:
        print "Case #%d: NO" % (case)
    else:
        i=len(candies)-1
        while i > 0:
            leftside = candies[:i]
            rightside = candies[i:]
            if xorit(leftside) == xorit(rightside):
                print "Case #%d: %d" % (case,sumit(leftside))
                break
            i-=1
        
    case +=1
