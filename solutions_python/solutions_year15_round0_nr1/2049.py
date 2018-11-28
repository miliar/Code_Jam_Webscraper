#!/usr/bin/python


import sys

try:
    f = open(sys.argv[1], "r");
except:
    sys.exit();



count = int(f.readline())
i = 1

while i <= count:
    line = f.readline().strip()
    #print line
    (smax, values) = line.split(" ")
    #print smax, values
    
    standing = 0
    friends = 0
    k = 0
    while k < len(values):
        if k == 0:
            standing = standing + int(values[0])
        else:
            oldStanding = standing
            standing = standing + int(values[k])
            if oldStanding < k:
                friends = friends + 1
                standing = standing + 1
            
        k = k + 1
    print "Case #%d: %d" %(i, friends)
    i = i + 1
        
