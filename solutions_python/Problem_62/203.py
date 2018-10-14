file = "A-large.in.txt"

data = [ l.strip().split()  for l in open(file).read().split('\n') ]

lines = int(data[0][0])


l = 1
for i in xrange(lines):
    T= int( data[l][0] ) 
    AB = []
    l+=1
    for j in xrange(T):
        AB.append( [int(data[l][0]), int(data[l][1])] )
        l+=1

    cnt = 0
    for j in xrange(T):
        for k in xrange(j+1,T):
            if (AB[j][0] > AB[k][0] and AB[j][1] > AB[k][1]):
                continue
            if (AB[j][0] < AB[k][0] and AB[j][1] < AB[k][1]):
                continue
            cnt+=1
    print "Case #%d: %d" % (i+1, cnt)