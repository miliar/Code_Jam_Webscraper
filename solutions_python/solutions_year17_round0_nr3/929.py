def getMaximum(a,b):
    if a > b:
        return a
    else:
        return b
def getMinimum(a,b):
    if a < b:
        return a
    else:
        return b
def fun1(n):
    if n%2 == 1:
        return [n/2,n/2]
    else:
        return [(n/2)-1,n/2]
def fun(segmentSize,k,opt,optPlus):
    if k > optPlus + opt:
        newOpt = 0
        newOptPlus = 0
        if segmentSize%2 == 1:
            newOpt = 2*opt + optPlus
            newOptPlus = optPlus
            return fun(segmentSize/2,k-(opt+optPlus),newOpt,newOptPlus)
        else:
            newOpt = opt
            newOptPlus = opt + 2*optPlus
            return fun((segmentSize/2)-1,k-(opt+optPlus),newOpt,newOptPlus)
    else:
        if k <= optPlus:
            return fun1(segmentSize+1)
        else:
            return fun1(segmentSize)



t = int(raw_input())
i = 1
while i <= t:
    n,k = map(int,raw_input().split())
    l,r = fun(n,k,1,0)
    maximum = getMaximum(l,r)
    minimum = getMinimum(l,r)
    print "Case #" + str(i) + ": " + str(maximum) +" "+ str(minimum)
    i += 1
