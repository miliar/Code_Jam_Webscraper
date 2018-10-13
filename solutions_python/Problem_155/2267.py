f = open('/Users/xiangjiang/Documents/git/googlecodejamxiang/A-large.in.txt', 'r')
testSize = int(f.readline())
testCases = []
for i in range(testSize):
    testCases = testCases + [f.readline().split()]
f.close()
fwrite = open('/Users/xiangjiang/Documents/git/googlecodejamxiang/result1_3', 'w')
caseNum = 1
for case in testCases:
    result = solve(int(case[0]), case[1])
    fwrite.write("Case #" + str(caseNum) + ":" + str(result) + "\n")
    caseNum += 1
fwrite.close()


def solve(maxShyness, members):
    currentSize = 0
    additionalSize = 0
    # iterate over all shyness levels
    for currentShyness in range(maxShyness + 1):
        print "\n[current iteration of shyness is: ", currentShyness, "]\n"
        # add to ovation if current ovation size is larger than current shyness level
        if currentSize >= currentShyness:
            currentSize += int(members[currentShyness])
            print "currentSize: ", currentSize
        # add to additionalSize if the current ovation size is smaller than current shyness level
        else:
            diff = currentShyness - currentSize
            print "Adding ", diff, " friends"
            additionalSize += diff
            currentSize += diff + int(members[currentShyness])
            print "Additional size is now: ", additionalSize
            print "Current size: ", currentSize
    print "result is: ", additionalSize

