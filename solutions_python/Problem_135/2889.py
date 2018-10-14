#!/usr/bin/python

myFile = open("inputMagician.txt")
nCases = (int)(myFile.next())

for i in xrange(nCases) : 
    curCase = i+1

    ans1 = (int)(myFile.next())
    field1 = [myFile.next() for x in xrange(4)]
    ans2 = (int)(myFile.next())
    field2 = [myFile.next() for x in xrange(4)]

    row1 = field1[ans1-1].split()
    row2 = field2[ans2-1].split()

    res = 0
    for val in row1 : 
        if val in row2 :
            res = res + 1
            myVal = val

    if res == 0 :
        print "Case #%d: Volunteer cheated!" % curCase
    elif res == 1 :
        print "Case #%d: %s" % (curCase,myVal)
    else :
        print "Case #%d: Bad magician!" % curCase
