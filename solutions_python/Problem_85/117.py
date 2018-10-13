fin = open("B-small-attempt1.in")
#fin = open("B-test.in")
fout = open("B-small.out", "wt")

def output(string):
    print string
    fout.write(string)
    
    
numCases = int(fin.readline().strip())
for caseIndex in range(1,numCases+1):
    # Code comes here
    nums = map(int, fin.readline().strip().split(" "))
    L = nums[0]
    t = nums[1]
    N = nums[2]
    C = nums[3]
    positions = []
    for i in range(0,C):
        positions.append(nums[4+i])
    mindist = min(positions)
    sortedpos = list(positions)
    sortedpos.sort()

    stars = [0] * (N+1)
    diffs = [0] * N
    for i in range(1,N+1):
        diffs[i-1] = positions[(i-1)%C]
        stars[i] = stars[i-1] + diffs[i-1] #positions[(i-1)%C]
    output("Case #%d: "% caseIndex)
    #print "mindist: %d" % mindist
    #print "positions: %s" % ",".join(map(str, positions))
    #print "stars: %s" % ",".join(map(str, stars))
    #print "diffs: %s" % ",".join(map(str, diffs))
    totaltime = stars[N]*2

    if t>totaltime:
        output("%d\n" % totaltime)
    else:
        firstStar = 0
        for i in range(1, N+1):
            if stars[i]*2>t:
                firstStar = i-1
                break
        remaining = list(diffs[firstStar+1:]) # add all full cycles
        remaining.append(stars[firstStar+1]-t*0.5) # add the first half cycle
        #print "Cutoff at star %d, %d" % (firstStar, stars[firstStar])      
        #print "Remaining: " + str(remaining)
        #print "L: %d" % L
        remaining.sort()
        # pop stars
        for i in range(0, L):
            m = max(remaining)
            #print "Pop %d" % m
            totaltime -= m
            remaining.remove(m)
        output("%d\n" % int(totaltime))
fin.close()
fout.close()
