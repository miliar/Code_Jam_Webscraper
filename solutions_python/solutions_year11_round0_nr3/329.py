#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gjam import *

qNum = ReadLInt()

#debugMode = True
debugMode = False

def dprint(str):
	if debugMode :
		print str
def has(alist,item):
	try :
		i = alist.index(item)
		return True
	except :
		return False


for q in xrange(qNum):

	pileNum = ReadLInt()

	piles = ReadLSplitInt()

	# 解く問題
	if debugMode and q != 2 :
		continue

	piles.sort()

	tryCount = pileNum*pileNum/2

	sNumSum = 0
	bNumSum = 0

	sBitSum = 0
	bBitSum = 0

	for candyNum in piles :
		bNumSum += candyNum 
		bBitSum = bBitSum ^ candyNum


	# この時点で、bBitSumが0でなければ、No判断でよいかと
	if bBitSum != 0 :
		PrintA(q,'NO')
		continue
	
	PrintA(q,bNumSum-piles[0])

#	maxSeanCandy = -1
#
#	dprint("0:S("+str(bNumSum)+","+str(sNumSum)+"),R("+str(bBitSum)+","+str(sBitSum)+")")
#
#	for i in xrange(tryCount) :
#
#
#		for j in xrange(pileNum) :
#			
#			dprint("  "+str(j)+":"+str(piles[j]))
#			
#			candyNum = piles[j]
#
#			nowBit = ((i+1)>>j) & 1 
#			preBit = (i>>j) & 1 
#
#			if nowBit == 1 and preBit == 0 :
#				# Big->Smallへ
#				bNumSum -= candyNum
#				sNumSum += candyNum
#				bBitSum = bBitSum ^ candyNum
#				sBitSum = sBitSum ^ candyNum
#
#				dprint("b->s")
#
#			elif nowBit == 0 and preBit == 1 :
#				# Small->Bigへ
#				bNumSum += candyNum
#				sNumSum -= candyNum
#				bBitSum = bBitSum ^ candyNum
#				sBitSum = sBitSum ^ candyNum
#
#				dprint("s->b")
#
#		dprint(str(i+1)+":S("+str(bNumSum)+","+str(sNumSum)+"),R("+str(bBitSum)+","+str(sBitSum)+")")
#
#		if bBitSum == sBitSum :
#			# 弟納得
#			if bNumSum > sNumSum :
#				seanCandy = bNumSum
#			else :
#				seanCandy = sNumSum
#			if maxSeanCandy < seanCandy :
#				maxSeanCandy = seanCandy
#				
#	if maxSeanCandy == -1 :
#		PrintA(q,'NO')
#	else :
#		PrintA(q,maxSeanCandy)
#
#	if debugMode :
#		break


	


