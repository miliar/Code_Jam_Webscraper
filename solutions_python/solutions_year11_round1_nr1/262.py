#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gjam import *

qNum = ReadLInt()

debugMode = False

def dprint(str):
	if debugMode :
		print str

def checkRank(num):

	if ( num == 100 or num == 0 ):
		return 1
	
	if num == 50 :
		return 2

	if ( num == 25 or num == 75 ) :
		return 4

	a = int( num / 20 )
	if a * 20 == num :
		return 5

	a = int( num / 10 )
	if a * 10 == num :
		return 10
	
	a = int( num / 4 )
	if a * 4 == num :
		return 25

	a = int( num / 2 )
	if a * 2 == num :
		return 50

	return 100


for q in xrange(qNum):
	
	items = ReadLSplitInt()
	
	N = items[0]
	PD = items[1]
	PG = items[2]
		
	dprint("=*="+str(q)+":"+str(N)+":"+str(PD)+":"+str(PG))

	todayRank = checkRank(PD)

	dprint( todayRank )

	# 今日は駄目か
	if todayRank > N :
		dprint("今日でOUT")

		# 今日でOUT
		PrintA(q,"Broken")
	else :

		# 全体は0or100ならOUT
		if ( PG == 0 and PD != 0 ) or ( PG == 100 and PD != 100 ) :
			PrintA(q,"Broken")
		else :
			PrintA(q,"Possible")





