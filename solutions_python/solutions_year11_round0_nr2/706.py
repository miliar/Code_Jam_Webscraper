import sys

def transform(stack, cList):
    if len(stack) < 2:
        return (stack, False)
    
    eos = stack[-2:]
    for comb in cList:
        if (comb[0] == eos[0] and comb[1] == eos[1]) or (comb[0] == eos[1] and comb[1] == eos[0]):
            stack = stack[0:-2]
            stack.append(comb[2])
            return (stack, True)
    return (stack, False)

def oppose(stack, oList):
    for comb in oList:
        if (comb[0] == comb[1] and stack.count(comb[0]) > 1) or (comb[0] in stack and comb[1] in stack):
            stack = []
            return (stack, False)
    return (stack, True)

def solve(cList, oList, eList):
    stack = []
    for i in xrange(len(eList)):
        stack.append(eList[i])
        processable = True
        while processable:
            stack, processable = transform(stack, cList)
            stack, p2 = oppose(stack, oList)
            processable = processable and p2
    return stack

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >> sys.stderr, "usage: %s <file>" % (sys.argv[0])
        quit()

    f = open(sys.argv[1])
    testCases = int(f.readline())
    print >> sys.stderr, "%d test cases" % testCases

    for i in xrange(testCases):
        caseData = f.readline().split()
        
        combinations = int(caseData[0])
        oppositions = int(caseData[combinations + 1])
        elements = int(caseData[combinations + oppositions + 2])

        print >> sys.stderr, "Combinations: %d\tOppositions: %d\tElements: %d" % (combinations, oppositions, elements)

        cList = caseData[1:combinations + 1]
        oList = caseData[combinations + 2:combinations + oppositions + 2]
        eList = caseData[combinations + oppositions + 3]
        output = solve(cList, oList, eList)
        print "Case #%d: [%s]" % ((i + 1), ", ".join(output))


