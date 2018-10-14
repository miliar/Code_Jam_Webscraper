import sys

name = "B-small-attempt0"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    # numberStr = str(input())
    number = long(input())
    # print(number)
    
    tidy = 1
    if len(str(number)) == 1:
        print("Case #" + str(testCase) + ": " + str(number))
    else:
    
        for x in xrange(number, 0, -1):
            xStr = str(x)
            # print('passei 1 for')
            cres = True
            for i in range(0, len(xStr)-1):
                # print('passei 2 for')
                if xStr[i] > xStr[i+1]:
                    cres = False
                    break
            if cres == True:
                tidy = x
                break
                
                
                # print(xStr[i])
        print("Case #" + str(testCase) + ": " + str(tidy))