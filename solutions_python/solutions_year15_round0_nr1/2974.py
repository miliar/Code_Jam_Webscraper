#!/usr/bin/env python

l = raw_input()

size=int(l)

for i in range(0, size):
    l = raw_input()
    s_max=l.split()[0]
    prob=l.split()[1]
    #print "s_max=" + s_max + ", problem=" + prob

    standing = 0
    friend = 0
    for j in range(0, len(prob)):
        if( j > standing and int(prob[j]) != 0 ):
            friend = friend + j - standing
            standing = j
            #print("a")
        standing = standing + int(prob[j])
        #print "standing=" + str(standing) + ", friend=" + str(friend) + ", prob[j]=" + str(prob[j]) + ", j=" + str(j)

    print "Case #" + str(i+1) + ": " + str(friend)
