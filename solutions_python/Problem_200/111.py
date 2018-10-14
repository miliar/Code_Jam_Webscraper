from collections import defaultdict
import sys

def testCase(args):
    intArray = [int(x) for x in str(args)]
    currentDigit = 0
    count = 0
    for i,x in enumerate(intArray):
        #print x, i, currentDigit,  intArray
        if x < currentDigit:
            # Bad, Subtract 1 from all
            #print count
            #print len(intArray) - i + count
            #if x == 0:
                #print str(int("".join(map(str,(intArray[0:i-count])))) - 1 )
                #print "9" * (len(intArray) - i - count)
            return str(int("".join(map(str,(intArray[0:i-count])))) - 1 ) + "9" * (len(intArray) - i + count)
            #else:
            #    return str(int("".join(map(str,(intArray[0:i])))) - 1) + "9" * (len(intArray) - i)
        elif x == currentDigit:
            count += 1
        else: #x > currentDigit
            currentDigit = x
            count = 0
    return args





testcount = int(sys.stdin.readline())
for i in range(testcount):
    line = sys.stdin.readline()
    #answer = testCase(map(int, line.split(" ")))
    answer = testCase(int(line))
    answer = int(str(answer))

    if answer != int(testCase(int(answer))):
        print "Error"
        sys.exit(1)
    print("Case #{}: {}".format(i+1, answer))
