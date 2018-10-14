import bisect

def giveMeBath(numOfStall, pplin):
    #pplin = [i for i,x in enumerate(bath) if x==1]
    if len(pplin) == 0:
        pplin = [0,numOfStall+1]
        maxplace = (0,numOfStall+1)
    else:
        keys = zip(pplin, pplin[1:])
        diff = [x[1]-x[0] for x in keys]
        maxplace = keys[diff.index(max(diff))]
    if (maxplace[1]-maxplace[0])%2==0:
        selected = (maxplace[0] + maxplace[1])/2
    else:
        selected = (maxplace[0] + maxplace[1] -1)/2
    bisect.insort(pplin,selected)
    return pplin

def placePeople(numOfStall, numOfPeople):
    if numOfStall == numOfPeople:
        return 0,0
    elif numOfPeople == 1:
        if numOfStall%2==0:
            return numOfStall/2, (numOfStall/2)-1
        else:
            return (numOfStall-1)/2,(numOfStall-1)/2
    else:
        pplin = []
        for i in xrange(numOfPeople-1):
            pplin = giveMeBath(numOfStall,pplin)
        return giveMeResult(pplin)

def giveMeResult(pplin):
    keys = zip(pplin, pplin[1:])
    diff = [x[1]-x[0] for x in keys]
    maxplace = keys[diff.index(max(diff))]
    if (maxplace[1]-maxplace[0])%2==0:
        selected = (maxplace[0] + maxplace[1])/2
    else:
        selected = (maxplace[0] + maxplace[1] -1)/2
    right = maxplace[1] - (selected+1)
    left = selected - (maxplace[0]+1)
    return max(left, right), min(left, right)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    ma ,mi = placePeople(n,m)
    print("Case #{}: {} {}".format(i, ma, mi))
