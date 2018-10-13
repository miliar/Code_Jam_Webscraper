#!/usr/bin/python

import sys

ipt = []
src = []


def read():
    return sys.stdin.readlines()

def getWP( asch ):
	games = 0
	score = 0
	for game in asch:
		if game == '.':
			continue
		else:
			games += 1
			score += int( game )
	return score*1.0 / games

def getOWP( mindex, sch ):
	count = 0
	sumWP = 0
	for i in range( len( sch ) ):
		if i == mindex or sch[i][mindex] == '.':
			continue
		else:
			count += 1
			asch = sch[i]
#			asch[mindex] = '.'
			newasch = asch[:mindex] + '.' + asch[mindex+1:]
			sumWP += getWP( newasch )
	return sumWP * 1.0 / count

def getOOWP( OWPList, i, sch ):
	count = 0
	oOWP  = 0
	for j in range( len( OWPList ) ):
		if sch[i][j] == '.':
			continue
		else:
			count += 1
			oOWP  += OWPList[ j ]

	return 1.0 *  oOWP  / count

def test( sch ):
	WPList = []
	OWPList = []
	OOWPList = []
	for i in range( len( sch ) ):
		WPList.append( getWP( sch[ i ] ) )
		OWPList.append( getOWP( i, sch ) )

	for i in range( len( sch ) ):
		OOWPList.append( getOOWP( OWPList, i, sch ) )
		print( 0.25* WPList[i] + 0.50 * OWPList[i] + 0.25* OOWPList[i] )


def runtest():
    readp = 0
    for x in range(cases):
        #TODO :implement test code
	teams = int(ipt[ readp + 1 ])
	sch = []
	for i in range( teams ):
		sch.append( ipt[ readp + 2 + i ][:-1] )
        print "Case #" + str(x + 1) + ":"
	test( sch )
	readp += 1 + teams


if __name__ == '__main__':
    ipt = read()
    cases = int( ipt[0] )
    runtest()



