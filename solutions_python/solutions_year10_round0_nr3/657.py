#!/usr/bin/python
import sys
import coaster

file = open(sys.argv[1], "r")
t = int(file.readline())
ii = 0;
while (ii < t):
    conf = file.readline ()
    conf = conf.strip ()
    conf = conf.split(" ")
    list = file.readline ()
    list = list.strip ()
    list = list.split(" ")
    ii = ii + 1
    co = coaster.coaster (int(conf[0]), int(conf[1]))
    sum = 0;
    for j in xrange(len(list)):
        sum = sum + int(list[j])

    if (sum < int(conf[1])):
        rev = co.rounds * sum
        co.setRevenue (rev)
    else:
        for i in xrange (co.rounds):
            lsize = len(list)
            for j in xrange(lsize):
                x = list.pop(0)
                if (not ((int(x) + co.getLoad()) > co.getSize())):
                    co.Load(int(x))
                    list.append(x)
                else:
                    list.insert(0,x)
            co.run ()
            co.unLoad ()
    print "Case #"+str(ii)+": "+str(co.getRevenue ())


    
