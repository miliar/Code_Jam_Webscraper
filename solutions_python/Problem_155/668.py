# Windows 8.1 python 2.7.9

fIn = "A-small-attempt1.in"

with open(fIn) as pAIn:
    contents = pAIn.readlines()

numCases = int(contents[0])
for case in range(1,numCases+1):
    thisCase = contents[case]

    maxShyness = int(thisCase[0])
    invited = 0
    standing = 0
    for shyness in range(0,maxShyness+1):
	numShy = int(thisCase[shyness+2])
	standing += numShy
	if numShy == 0 and (standing + invited) <= shyness:
	    invited += 1

    #print "Case #" + str(case)+": "+str(invited)
    print 'Case #{0:d}: {1:d}'.format(case,invited)

