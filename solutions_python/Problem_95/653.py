#From https://code.google.com/codejam/contest/351101/dashboard#s=p0
#Problem A. Store Credit

import sys
import string

sys.stdout.softspace = 0

MY_DEBUG = False


myMap = dict([("y", "a"), ("e", "o"), ("q", "z"), ("z", "q")]) #Inverse mapping (decryption key)

#Encription key
#myMap2 = dict()
myMap2 = dict([("a", "y"), ("o", "e"), ("z", "q"), ("q", "z")])

def ReadDataToCreateMapping(fileName):
    f = open(fileName, "rb")

    T = int(f.readline())
    if (MY_DEBUG):
        print "T =", T

    fOut = open("A_training.out", "rb")

    for i in range(1, T + 1):
        line = f.readline().rstrip()

        lineOut = fOut.readline().rstrip()
	lineOut = lineOut[9:]
        if (MY_DEBUG):
            print line
            print lineOut

        for strIndex in range(len(line)):
	    if (line[strIndex] in myMap):
                #if (myMap2[lineOut[strIndex]] == line[strIndex]):
                if (myMap[line[strIndex]] == lineOut[strIndex]):
		    if (MY_DEBUG):
	        	#print "Not adding again for %s" % (lineOut[strIndex])
	        	print "Not adding again for %s" % (line[strIndex])
        	    pass
                else:
		    if (MY_DEBUG):
        		#print "ERROR: %s should map to %s, but now it is mapped to %s" % (lineOut[strIndex], myMap2[lineOut[strIndex]], myMap2[line[strIndex]])
        		print "ERROR: %s is map for %s, but now it is mapped for %s" % (line[strIndex], myMap[line[strIndex]], myMap[lineOut[strIndex]])
        	    pass
	    else:
                myMap[line[strIndex]] = lineOut[strIndex]
                myMap2[lineOut[strIndex]] = line[strIndex]
		if (MY_DEBUG):
            	    print "%s <- %s\n" % (line[strIndex], lineOut[strIndex])
            #print "line[j] = %s, %d\n" % (line[j], ord(line[j]))

    #print "myMap =", myMap
    #print "myMap2 =", myMap2

    if (MY_DEBUG):
	print "myMap"
        for k, v in sorted(myMap.iteritems()):
    	    print k, v
	print "myMap2"
	for k, v in sorted(myMap2.iteritems()):
    	    print k, v

        #print "Sorted Keys: ", sorted(myMap.keys())
        #print "Sorted Vals: ", sorted(myMap.values())

        print "Sorted Keys: ", sorted(myMap.keys())
        print "Sorted Vals: ", sorted(myMap.values())

    f.close()
    fOut.close()


def ReadData(fileName):
    f = open(fileName, "rb")

    T = int(f.readline())

    if (MY_DEBUG):
        print "T =", T

    for i in range(1, T + 1):
        line = f.readline().rstrip()
	if (MY_DEBUG):
    	    print line

	lineDecrypted = ""
	
        for strIndex in range(len(line)):
            #myMap[line[strIndex]] = line[strIndex]
            lineDecrypted += myMap[line[strIndex]]

	#print "Translation: ", lineDecrypted
	print "Case #%d: %s" % (i, lineDecrypted)


    f.close()
    #fOut.close()


#"Training" the mapping
ReadDataToCreateMapping("A_training.in")

#ReadData("A.in")
ReadData("A-small-attempt0.in")
