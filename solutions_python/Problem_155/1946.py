lines = [line.strip() for line in open('large.in')]

#print lines
T = int(lines.pop(0))
#print T

for i in range(T):
    line = str(lines.pop(0))
    [maxS, s] = line.split(' ')
    maxS = int(maxS)
    count = 0
    needed = 0

    #print line
    for c in range(maxS + 1):

        #print c, s[c], count

        if count < c:
            #print "WE NEED MORE"
            needed += 1
            count += 1

        count += int(s[c])

    print "Case #%d: %d" % (i+1, needed)
