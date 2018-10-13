import sys
fh = open(sys.argv[1], "r")
T= int(fh.readline())
for i in xrange(T):
    [a,b] = map(int, fh.readline().split(" "))
    dict = {}
    numpairs = 0
    for j in xrange(a,b+1):
        if j not in dict:
            l = str(j)
            r = [j]
            for k in range(1,len(l)):
                newj = int(''.join(l[k:]+l[:k]))
                if newj >=a and newj <= b and newj not in r:
                    r.append(newj)
            if len(r) > 1:
                numpairs+= (len(r)-1)*len(r)/2
            for k in r:
                dict[k] = True
    print "Case #{0}: {1}".format(i+1, numpairs)
fh.close()
            
