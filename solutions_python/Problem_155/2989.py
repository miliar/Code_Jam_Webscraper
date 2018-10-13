#!/usr/bin/python

import sys

def process(crowd):
    #print crowd
    part_sum = 0
    friend = 0

    for i in range(len(crowd)):
        c = int(crowd[i])
        friend_needed = 0
        if (i > part_sum):
            friend_needed = i - part_sum
        friend += friend_needed
        part_sum += c + friend_needed
    return friend

fin = open(sys.argv[1], 'r')

fout = open(sys.argv[1].split(".")[0] + ".out", "w")

nb_cases = int(fin.readline())

for i in range(1, nb_cases + 1):
    line = fin.readline().strip().split(" ")
    print "Case #%d" % (i)
    fout.write("Case #%d: %s\n" % (i, process(line[1])))

fout.flush()
fout.close()
fin.close()



# print "toto"
