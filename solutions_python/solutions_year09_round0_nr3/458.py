f=open("C-small-attempt0.in")
cases=int(f.readline())
teststr="welcome to code jam"
for i in xrange(1,cases+1):
    raw=f.readline()
    testgrid=[1]
    for j in xrange(len(teststr)):
        testgrid.append(0)
    for x in raw:
        for y in range(len(teststr)):
            if x==teststr[y]:
                testgrid[y+1]+=testgrid[y]
    x=testgrid[-1]%1000
    if x<10:
        print "Case #"+str(i)+": 000"+str(x)
    elif x<100:
        print "Case #"+str(i)+": 00"+str(x)
    elif x<1000:
        print "Case #"+str(i)+": 0"+str(x)
    else:
        print "Case #"+str(i)+": "+str(x)
