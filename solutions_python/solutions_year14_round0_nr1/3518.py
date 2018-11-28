#!/usr/bin/python2.7

import sys

fname = sys.argv[1]

count = 0
ans1 = 0
ca1 = 0
ans2 = 0
ca2 = 0
dcount = 0
l1 = []
l2= []

with open(fname) as f:
    for line in f:
        if (count == 0):
            count = int(line)
#            print "Count of Tests: %s" % count
            continue
        if (ans1 == 0):
            ans1 = int(line)
 #           print "ans1: %s" % ans1
            continue
        if (ca1 != 4):
            ca1 += 1
            if (ans1 != 9):
                ans1 -= 1
                if (ans1 == 0):
                    ans1 = 9
                    l1 = (line.split("\n")[0]).split(" ")
                    #continue
                else:
                    continue
            continue
        if (ans2 == 0):
            ans2 = int(line)
  #          print "ans2: %s" % ans2
            continue
        if (ca2 != 4):
            ca2 += 1
            if (ans2 != 9):
                ans2 -= 1
                if (ans2 == 0):
                    ans2 = 9
                    l2 = (line.split("\n")[0]).split(" ")
                   # continue
                else:
                    continue
            if (ca1 + ca2 == 8):
                ca1 = 0
                ca2 = 0
                ans1 = 0
                ans2 = 0
                dcount += 1
                res = filter(lambda x: x in l1, l2)
                if (len(res) != 0):
                    if (len(res) == 1):
                        print "Case #%s: %s" % (dcount, res[0])
                    else:
                        print "Case #%s: Bad magician!" % dcount
                else:
                    print "Case #%s: Volunteer cheated!" % dcount
            continue
