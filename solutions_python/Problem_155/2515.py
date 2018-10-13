testcases = int(raw_input())

for i in range(testcases):
    maxShyness, shyness = raw_input().split()
    maxShyness = int(maxShyness)
    totalCount = int(shyness[0])
    needToBeInvited = 0
    for j in range(1,maxShyness+1):
        if(int(shyness[j]) >= 1 and j>=totalCount):
            needToBeInvited += (j - totalCount)
            totalCount += (j - totalCount)
        totalCount+= int(shyness[j])
    print "Case #%d: %d" % (i+1, needToBeInvited)
           
