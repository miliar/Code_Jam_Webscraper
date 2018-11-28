import sys
import fileinput
import re

def makeRegex(msg):
    ret = msg.replace("(", "[")
    ret = ret.replace(")", "]")
    return ret

def processInput():
    tcIn = fileinput.input()
    wordSize, dictSize, tcCount = (int(x) for x in tcIn.readline().split())
    dictionary = []
    for i in range(dictSize):
        dictionary.append(tcIn.readline())
    assert len(dictionary) == dictSize
    messages = []
    for i in range(tcCount):
        message = tcIn.readline()
        print "Case #%d: %d" % (i+1, matchCount(dictionary, message))

def matchCount(dict, msg):
    msg = makeRegex(msg)
    count = 0
    for w in dict:
        if re.search(msg, w):
            count += 1
    return count

def main():
    #testcases = readInput();
    #for i, tc in enumerate(testcases):
        #print "Case #%d: %d" % (i+1, countSwitches(tc[0], tc[1]))

    processInput()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
