#!/bin/python
caseCount = int(input())
for h in range(1,caseCount+1):
    # print("newcase")
    # case start
    size,people = [int(n) for n in input().split(" ")]

    while(people>0):
        # print("size: " + str(size) + ", people: " + str(people))
        s1=size//2      # could be greater
        s2=size-s1-1
        p1=people//2
        p2=people-p1-1    # could be greater

        # if s1==s2: # take same size and more people
            # size = s1 #s2
            # people = p1
        # else
        if p1==p2: # take smaller size and same people
            size = s2
            people = p1 #p2
        else: # different people and different size
            size = s1
            people = p1

    print("Case #{}: {} {}".format(h,s1,s2))
    # case end
