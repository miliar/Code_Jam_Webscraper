def ovation():
    fields = raw_input().strip().split(' ')
    levels = fields[1]
    prevcount = int(levels[0])
    addition = 0
    for i in xrange(1,len(levels)):
        if(int(levels[i])!=0):
            curadd = max(0,i-prevcount)
            addition += curadd
            prevcount += curadd
        prevcount += int(levels[i])
    return addition

ncases = int(raw_input().strip())
for i in xrange(ncases):
    print "Case #{0}: {1}".format(i+1, ovation())
