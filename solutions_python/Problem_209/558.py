from math import pi

cases = input()

for i in range(cases):
    cakes,stack = map(int,raw_input().split())
    cakelist = []
    for j in range(cakes):
        radius,height = map(int,raw_input().split())
        cakelist.append((2*pi*radius*height,radius))
    #import pdb;pdb.set_trace()
    cakelist.sort()
    if stack>1:
        outputlist = cakelist[-stack+1:]
    else:
        outputlist = []
    if outputlist:
        sidesum = sum([item[0] for item in outputlist])
        maxradius = max([item[1] for item in outputlist])
    else:
        sidesum = 0
        maxradius = 0
    optindex = 0
    optradius = max(maxradius,cakelist[0][1])
    optvalue = sidesum + cakelist[0][0] + pi*optradius*optradius
    for j in range(1,cakes-stack+1):
        optradius = max(maxradius,cakelist[j][1])
        testvalue = sidesum + cakelist[j][0] + pi*optradius*optradius
        if testvalue>optvalue:
            optindex = j
            optvalue = testvalue
    print "CASE #%d: %.7f"%(i+1,optvalue)

