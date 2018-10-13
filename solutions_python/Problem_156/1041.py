import math
import sys
import heapq as hq

poss = {}
for i in range(1,1001):
    poss[i] = {}
    for j in range(1,i+1):
        numsplits = j-1
        maxbin = int(math.ceil(i*1.0/j))
        #print(" ".join([str(x) for x in [i,numsplits,maxbin]]))
        poss[i][maxbin] = min(poss[i].get(maxbin,numsplits),numsplits)

f = open(sys.argv[1])
f.readline()

t = 1
l = f.readline()
while l != "":
    diners = [int(x) for x in f.readline().split()]
    counts = [(x,diners.count(x)) for x in set(diners)]
    counts.sort()


    best = counts[-1][0]
    h = []
    hq.heappush(h,(0,len(counts)-1,0,0))

    tested = set()
    while len(h)>0:
        x = hq.heappop(h)
        cumtime,i,splittime,eattime = x
        if (i,splittime,eattime) in tested:
            continue
        tested.add((i,splittime,eattime))
        if cumtime > best:
            continue

        numcakes,cakecounts = counts[i]
        newcounts = i-1

        for time,numsplits in poss[numcakes].items():
            newsplit = splittime + numsplits*cakecounts
            neweat = max(eattime,time)
            if newcounts < 0:
                best = min(best,newsplit+neweat)
            else:
                hq.heappush(h,(newsplit+neweat,newcounts,newsplit,neweat))
    print "Case #{}: {}".format(t,best)
    t += 1
    l = f.readline()
