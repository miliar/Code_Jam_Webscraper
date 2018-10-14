f = open('/home/michael/Dropbox/Code Jam/2012/Recycled Numbers/Inreal.in','r')
numcases = int(f.readline())
for x in range(numcases):
    print "Case #%d:" % (x+1),
    resultlist = []
    resultlist2 = []
    line = f.readline().split()
    low = int(line[0])
    high = int(line[1])
    for a in map(str, range(low,high + 1)):
        if len(str(low)) > 1:
            for b in range(1,len(str(low))):
                c = a[-b:]
                d = a[:-b]
                e = int(c + d) #new integer
                if (e < high or e == high) and (e != int(a)): #make sure not same #
                    if (e > low) or (e == low):
                        resultlist.append(int(a))
                        resultlist2.append(e)
    l = zip(resultlist, resultlist2)
    z = list(set(l))
    print len(z)/2 # I have no idea which number was repeated
