import sys, pdb
testcases = []

def getInput(filename):
    inputfile = open(filename)
    count = 0
    n = 0
    for line in inputfile:
        count += 1
        if count == 1:
            n = int(line.strip())
            continue
        testcases.append(line.strip())

def process(tc):
    tclen = len(tc)
    if len(tc) == 1:
        return tc
    break_index = -1
    j=k=None

    #Find break point
    for i in range(tclen-1):
        j = tc[i]
        k = tc[i+1] 
        if j > k:
           break_index = i

    # Return original number if no break point found
    if break_index == -1:
        return tc
    
    prefix = process(str(int(tc[:break_index+1])-1))
    suffix = ''.join(['9']*(tclen-len(prefix)))
    return str(int(prefix + suffix))

def processTestcases():
    count = 0
    for tc in testcases:
        count += 1
        result = process(tc)
        print "Case #%d: %s" % (count, result)
    

def main():
    #filename = "input/test_input.txt"
    filename = "input/B-small-attempt2.in.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    getInput(filename)
    processTestcases()

if __name__ == "__main__":
    main()
