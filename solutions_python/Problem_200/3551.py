#!/usr/bin/python

import sys, getopt

def isTidy(number):
    num = 0
    for i in number:
        if int(i) < num:
            return False
        num = int(i)
    return True

def tidy(number):
    lastTidy = []
    tidyUp = True
    for i in xrange(len(number)-1):
        first = int(number[i])
        second = int(number[i+1])
        if tidyUp:
            if first <= second:
                lastTidy.append(str(first))
            else:
                lastTidy.append(str(first-1))
                tidyUp = False
        else:
            lastTidy.append("9")
    if tidyUp:
        lastTidy.append(number[-1])
    else:
        lastTidy.append("9")
    newNumber = "".join(lastTidy)
    if isTidy(newNumber):
        return int(newNumber)
    else:
        return int(tidy(newNumber))
        

def main(argv):
    inputfile = None
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'flipPancakes.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'flipPancakes.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    f = open(inputfile, 'r')
    numTestCases = int(f.readline())
    for i in xrange(numTestCases):
        number = f.readline().strip()
        print "Case #"+str(i+1)+":", tidy(number)

if __name__ == "__main__":
    main(sys.argv[1:])
