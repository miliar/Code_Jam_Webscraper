#!/usr/bin/python -tt

import sys

def main():
    inFile = open(sys.argv[1], 'rU')
    outFile = open(sys.argv[2], 'w')
    aLine = inFile.readline()
    T = eval(aLine)
    for case in range(T):
        aLine = inFile.readline()
        aLine = aLine.split()
        nCommand = eval(aLine.pop(0))
        oPos = 1
        bPos = 1
        oTime = 0
        bTime = 0
        time = 0
        for i in range(nCommand):
            pos = eval(aLine[2*i+1])
            #print "pos = ", pos
            if aLine[2*i] == 'O':
                if abs(pos - oPos) - (time-oTime) <= 0:
                    time += 1
                else:
                    time += (abs(pos-oPos) - (time-oTime))+1
                oPos = pos
                oTime = time
            elif aLine[2*i] == 'B':
                #print "bPos = ", bPos
                if abs(pos - bPos) - (time-bTime) <= 0:
                    time += 1
                else:
                    time += (abs(pos-bPos) - (time-bTime))+1
                bPos = pos
                bTime = time
            #print "time = ", time
        print time
        outFile.write("Case #%d: %d\n" %(case+1, time))
    inFile.close()
    outFile.close()


if __name__ == '__main__':
    main()
