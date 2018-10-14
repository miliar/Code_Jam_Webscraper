import sys

def figureout(data):
    # check if its doable
    xtotal = 0
    for item in data:
        xtotal = xtotal ^ item

    if xtotal != 0:
        return "NO"
    else:
        return sum(data[1:])
        


def processtestcases():
    numtestcases = int(sys.stdin.readline().rstrip())
    testcases = []
    
    # read in instructions for each test case
    for i in range(numtestcases):
        sys.stdin.readline() # discard count
        inputs = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
        inputs.sort()
        testcases.append(inputs)
    return testcases


if __name__ == "__main__":
    testcases = processtestcases()
    #print str(testcases)
    i = 1
    for testcase in testcases:
        figure = figureout(testcase)
        print "Case #"+str(i)+": "+str(figure)
        i += 1


