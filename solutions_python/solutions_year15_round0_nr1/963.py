import sys

f = open(sys.argv[1])
n = int(f.readline())

for t in xrange(1,n+1):
    s = f.readline().strip("\n").split(" ")[1]
    rsum = int(s[0])
    maxd = 0
    for i in xrange(1,len(s)):
        if(i - rsum > maxd):
            maxd = i - rsum
        rsum += int(s[i])
    print "Case #%d: %d" % (t,maxd)


        










