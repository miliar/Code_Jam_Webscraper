#!/usr/bin/python

import sys, datetime, math

SEPARATE_LINE = "=" * 20



def solve(line, line2):
    v = line.split()
    v2 = line2.split()
    v2n = [int(i) for i in v2]
    v2n.sort()
    A = int(v[0])
    num = int(v[1])
    op = 0
    j = 0
    for i in v2n:
	if A>v2n[-1]:
		break
	elif A>i:
		A = A+i
	else:
		op2=0
		while A<=i:
			A=A+(A-1)
			op2=op2+1
			if op2==num-j:
				break
		op=op+op2		
		if op2==num-j:
			break
		A = A+i
	j=j+1	
    return str(op)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit();

    inFile = open(sys.argv[1])
    outFile = open(sys.argv[2], "w")

    startTime = datetime.datetime.now()
    print "Start Time = %s" % startTime
    print SEPARATE_LINE

    T = int(inFile.readline())
    for i in range(T):
        line = inFile.readline()
	line2 = inFile.readline()
        result = solve(line.strip(), line2.strip())
        outFile.write("Case #%d: %s\n" % (i + 1, result))
    endTime = datetime.datetime.now()

    print SEPARATE_LINE
    print "End Time = %s" % endTime
    print "Cost Time = %s" % (endTime - startTime)
    inFile.close()
    outFile.close()
