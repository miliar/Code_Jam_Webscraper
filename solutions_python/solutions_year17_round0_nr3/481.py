import sys, random

import psyco; psyco.full()

def solvecase(n, k):
    n += 2
    
    stalls = [0] * n
    stalls[0] = 1
    stalls[-1] = 1
    
    dists = [None] * n
    
    for i in xrange(k):
        #print "-----------------"
        for j in xrange(1, n-1):
            distL = 0
            while stalls[j-1-distL] != 1:
                distL += 1
                
            distR = 0
            while stalls[j+1+distR] != 1:
                distR += 1
            
            dists[j] = (distL, distR)
            
        #print dists
        
        best = None
        for j in xrange(1, n-1):
            if stalls[j] == 1:
                continue
            if best is None:
                best = min(dists[j])
            else:
                if min(dists[j]) > best:
                    best = min(dists[j])
        #print best
        
        cands = []
        for j in xrange(1, n-1):
            if stalls[j] == 1:
                continue
            if min(dists[j]) == best:
                cands.append((j, dists[j]))
        
        #print cands
        
        best = None
        for j in xrange(len(cands)):
            if best is None:
                best = max(cands[j][1])
            else:
                if max(cands[j][1]) > best:
                    best = max(cands[j][1])
                    
        for j in xrange(len(cands)):
            if max(cands[j][1]) == best:
                assert stalls[cands[j][0]] == 0
                stalls[cands[j][0]] = 1
                last = cands[j][1]
                break
        
        #print "".join(str(x) for x in stalls), last, bin(i+1), solvecase3(n-2, i+1)
        
    return last
    
def solvecase2(n, k):
    n += 2
    
    stalls = [0] * n
    stalls[0] = 1
    stalls[-1] = 1
    
    dists = [None] * n
    for j in xrange(1, n-1):
        distL = 0
        while stalls[j-1-distL] != 1:
            distL += 1
            
        distR = 0
        while stalls[j+1+distR] != 1:
            distR += 1
        
        dists[j] = (distL, distR)
        
    dists[0] = (-1, -1)
    dists[-1] = (-1, -1)
    
    for i in xrange(k):
        best = None
        for j in xrange(1, n-1):
            if stalls[j] == 1:
                continue
            if best is None:
                best = min(dists[j])
            else:
                if min(dists[j]) > best:
                    best = min(dists[j])
        #print best
        
        cands = []
        for j in xrange(1, n-1):
            if stalls[j] == 1:
                continue
            if min(dists[j]) == best:
                cands.append((j, dists[j]))
        
        #print cands
        
        best = None
        for j in xrange(len(cands)):
            if best is None:
                best = max(cands[j][1])
            else:
                if max(cands[j][1]) > best:
                    best = max(cands[j][1])
                    
        for j in xrange(len(cands)):
            if max(cands[j][1]) == best:
                lastn, lastdist = cands[j]
                break
        
        #print "------", lastn, lastdist, stalls
        
        assert stalls[lastn] == 0
        stalls[lastn] = 1
        
        #print dists
        distL = 0
        while stalls[lastn-1-distL] != 1:
            dists[lastn-1-distL] = (dists[lastn-1-distL][0], distL)
            distL += 1
        dists[lastn-1-distL] = (dists[lastn-1-distL][0], distL)
        
        distR = 0
        while stalls[lastn+1+distR] != 1:
            dists[lastn+1+distR] = (distR, dists[lastn+1+distR][1])
            distR += 1
        dists[lastn+1+distR] = (distR, dists[lastn+1+distR][1])
        
        #print dists
        
    return lastdist
    
def solvecase3(n, k):
    buckets = {n: 1}
    xcount = 2
    while k >= xcount:
        xcount <<= 1
        newbuckets = {}
        for size in buckets:
            count = buckets[size]
            low = (size - 1) / 2
            high = size - 1 - low
            
            if low not in newbuckets:
                newbuckets[low] = 0
            newbuckets[low] += count
            
            if high not in newbuckets:
                newbuckets[high] = 0
            newbuckets[high] += count
        
        buckets = newbuckets
        
    #print buckets, 
    target = k - (xcount / 2)
    buckets = sorted(buckets.items())[::-1]
    for size, count in buckets:
        if target < count:
            low = (size - 1) / 2
            high = size - 1 - low
            return low, high
        else:
            target -= count

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        n, k = [int(x) for x in f.readline().strip().split()]
        
        a, b = solvecase3(n, k)
                
        print "Case #%d: %d %d" % (caseno+1, b, a)
       

main()
#solvecase(42, 30)

# for i in xrange(1000):
    # a = random.randint(1, 150)
    # b = random.randint(1, a)
    # print a, b, solvecase(a, b), solvecase3(a, b)
    # assert solvecase(a, b) == solvecase3(a, b)
