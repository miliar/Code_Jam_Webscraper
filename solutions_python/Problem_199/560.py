#!/bin/python
caseCount = int(input())
for h in range(1,caseCount+1):
    # case start
    pancakes, breadth = (input().split(" "))

    breadth = int(breadth)
    pancakes = [ (x=="+") for x in pancakes]
    length  = len(pancakes)
    count = 0

    for i in range(length-breadth+1):
        # print("new index")
        if not pancakes[i]:
            # print("new flip")
            # need to flip
            count+=1
            for j in range(i,i+breadth):
                # print("count")
                # flip breadth many pancaces
                pancakes[j] = not pancakes[j]

    # now the first pancaces are right
    for i in range(length-breadth+1,length):
        if not pancakes[i]:
            count="IMPOSSIBLE"
    print("Case #{}: {}".format(h,count))
    # case end
