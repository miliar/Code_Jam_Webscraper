#!/usr/bin/python
import sys
import math

def snap_cal(switchcount, snapcount):
    change_value = int(math.pow(2, switchcount))
    if (1 == ((change_value - snapcount%change_value))):
        return "ON"
    else:
        return "OFF"

def snapper(filename, outputfile):
    lines = open(filename,'r').readlines()
    outputdata = ""
    testcase_count = int(lines[0])
    counter=1
    for line in lines[1:]:
        try:
            switchcount, snapcount=map(int,line.split())
        except Exception :
            counter = counter + 1
            continue
        snapresult = snap_cal(switchcount, snapcount)
        outputdata = outputdata  + "Case #%d: %s\n"%(counter, snapresult)
	counter = counter + 1
    outputdata = outputdata.strip()
    open(outputfile, 'w').write(outputdata)
    print outputdata

if __name__=="__main__":
    try:
        snapper(sys.argv[1], sys.argv[2])
    except Exception as e:
        print "Error cause :%s"%e
