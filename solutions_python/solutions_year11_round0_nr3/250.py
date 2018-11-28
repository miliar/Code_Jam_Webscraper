import sys,math

numOfTests= int(sys.stdin.readline())
for i in range(numOfTests):
    numOfCandies = int(sys.stdin.readline())
    Candies = sys.stdin.readline().split()
    
    # pat add in xor, op is ^
    xorsum = 0
    addsum = 0
    smallest = sys.maxint
    for c in Candies:
        xorsum = xorsum ^ int(c)
        addsum = addsum + int(c)
        smallest = min(smallest,int(c))
    if xorsum == 0:
        print "Case #" + str(i+1) + ": " + str(addsum - smallest)
    else:
        print "Case #" + str(i+1) + ": NO"