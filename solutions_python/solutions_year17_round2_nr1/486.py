#Joe Snider
#4/16
#
#code jam 2017, r2Ba

def doit(D, horseX, horseN):
    longestTime = 0
    for i in xrange(len(horseX)):
        ti = float(D-horseX[i])/float(horseS[i])
        #print "gh2",ti
        if ti > longestTime:
            longestTime = ti
    #print "gh1",longestTime, D
    ret = "%.7f"%(float(D)/float(longestTime),)
    return ret

#raw_imput is one line    
t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    D = int(line[0])
    N = int(line[1])
    horseX = []
    horseS = []
    for j in xrange(N):
        line2 = raw_input().split(" ")
        horseX.append(int(line2[0]))
        horseS.append(int(line2[1]))
    #print "gh3",horseX,horseS,D,N
    print "Case #%d: %s"%(i, doit(D, horseX, horseS))
