#From https://code.google.com/codejam/contest/351101/dashboard#s=p0
#Problem B. Store Credit

import sys
import string

sys.stdout.softspace = 0

MY_DEBUG = False
#MY_DEBUG = True


def Solve(t, N, S, p):
    yRes = 0
    numSuprisesLeft = S

    #print "t =", t
    #print "N = %d, S = %d, p = %d" % (N, S, p)

    for i in range(N):
	if (t[i] >= 3 * p): #No need to make this a surprise score 
	    yRes += 1
	    continue
	    
	if ( ((t[i] == 3 * p - 3) or (t[i] == 3 * p - 4)) and (p - 2 >= 0)):
	    """
	    This sum can have 1 or 2 of the three scores higher than p only if we make it a surprise.
	    More exactly:
		- if t[i] == 3*p - 4 --> solution with a match is [p, p-2, p-2]
		- if t[i] == 3*p - 3 --> solution with a match is [p, p-1, p-2]
	    """
	    if (numSuprisesLeft > 0):
		yRes += 1
		numSuprisesLeft -= 1

	    continue

	if ( ((t[i] == 3 * p - 2) or (t[i] == 3 * p - 1)) and (p - 1 >= 0)):
	#else: #(t[i] >= 3 * p - 2):
    	    """
	    if t[i] == 3*p - 2 --> solution with a match is [p, p-1, p-1] (or [p, p, p-2], which consumes a surprise)
	    if t[i] == 3*p - 1 --> solution with a match is [p, p-1, p]
    	    """
	    yRes += 1
	
	"""
	if (t[i] < 3 * p - 4): #This sum cannot have any of the three scores higher than p 
	    pass
	    #yRes += 0
	"""

    return yRes


def ReadData(fileName):
    f = open(fileName, "rb")

    T = int(f.readline())

    if (MY_DEBUG):
        print "T =", T

    for i in range(1, T + 1):
        line = f.readline().rstrip()
        lineList = string.split(line, " ")

	N = int(lineList[0])
	S = int(lineList[1])
	p = int(lineList[2])

	if (MY_DEBUG):
    	    print line
    	    print "N = %d, S = %d, p = %d" % (N, S, p)

	t = []
	for j in range(N):
	    t.append( int(lineList[j + 3]) )
	    #print "%d " % t[i]

	y = Solve(t, N, S, p)

	print "Case #%d: %d" % (i, y)

    f.close()
    #fOut.close()


#ReadData("B.in")
#ReadData("B-small-attempt0.in")
ReadData("B-large.in")
