#! /usr/bin/python

import sys

for i in range(int(sys.stdin.readline())):
    split = sys.stdin.readline().split()

    shyString = split[1]
    friends_inv = 0
    ppl_standing = 0
    for shy_level in range(int(split[0])+1):
        #print("ppl standing " + str(ppl_standing))
        #print(str(shy_level) + " : " +  shyString[shy_level])

        shy_ppl = int(shyString[shy_level])
        if shy_ppl == 0: 
            continue
        if shy_level <= ppl_standing:
            ppl_standing = int(shyString[shy_level]) + ppl_standing
        else:
            friends_inv = (shy_level - ppl_standing) + friends_inv 
            ppl_standing = int(shyString[shy_level]) + shy_level
    
    print("Case #" + str(i+1) + ": " + str(friends_inv))
