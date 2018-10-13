

        
def getTime(N, dists, t, starsWithBoosters, extra):
    currentTime = 0.0
    for star in range(0, N):
        dist = getDist(star, dists)
        if star in starsWithBoosters or star == extra:
            if currentTime < t:
                timeleft = t - currentTime
                if timeleft >= dist * 2:
                    currentTime += dist * 2
                else:
                    currentTime += timeleft  + (dist - timeleft /2)
            else:
                currentTime += dist
        else:
            currentTime += dist * 2
    return currentTime

def getDist(i, dists):
    return dists[i % len(dists)]

f = open('c.in')
T = int(f.readline())
for t1 in range(T):
    dists = []
    vals = map(int, f.readline().split())
    L, t, N, C = vals[:4]
    dists = vals[4:]
    starsWithBoosters ={}
    #print dists
    #print getDist(1, dists)
    minTime = getTime(N, dists, t, {}, -1)
    
    #print "mintime:", minTime
    if (L > 0) and minTime > t:
        boostersLeft = L
        starsWithBoosters = {}
        while boostersLeft > 0:
            bestBoosterPos = N
            for b1 in range(0,N):
                if (not b1 in starsWithBoosters):
                    time = getTime(N, dists, t, starsWithBoosters, b1)
                    if time < minTime:
                        minTime = time
                        bestBoosterPos = b1
            
            starsWithBoosters[bestBoosterPos] = True
            
            boostersLeft-=1
    
    print "Case #%d: %s" % (t1+1, int(minTime))