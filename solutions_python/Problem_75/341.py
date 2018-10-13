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

	items = ReadLSplit()

	#if q != 5 :
		#continue
	
	# 解釈
	combineRuleNum = int(items[0])
	combineRule = {
			'Q' : {},
			'W' : {},
			'E' : {},
			'R' : {},
			'A' : {},
			'S' : {},
			'A' : {},
			'D' : {},
			'F' : {} }
	opposedRule = {
			'Q' : [],
			'W' : [],
			'E' : [],
			'R' : [],
			'A' : [],
			'S' : [],
			'A' : [],
			'D' : [],
			'F' : [] }
	for item in items[1:combineRuleNum+1] :
		combineRule[item[0]][item[1]] = item[2]
		if item[0] != item[1] :
			combineRule[item[1]][item[0]] = item[2]

	opposedRuleNum = int(items[combineRuleNum+1])
	for item in items[combineRuleNum+2:combineRuleNum+opposedRuleNum+2] :
		opposedRule[item[0]].append( item[1] )
		if item[0] != item[1] :
			opposedRule[item[1]].append( item[0] )

	elementNum = int(items[combineRuleNum+opposedRuleNum+2])
	elementList = items[combineRuleNum+opposedRuleNum+3]

	dprint(combineRule)
	dprint(combineRuleNum)
	dprint(opposedRule)
	dprint(opposedRuleNum)
	dprint(elementNum)
	dprint(elementList)


	previousE = '-'
	ansString = ''
	
	elasePlace = {
			'Q' : [],
			'W' : [],
			'E' : [],
			'R' : [],
			'A' : [],
			'S' : [],
			'A' : [],
			'D' : [],
			'F' : []}

	for i in xrange(elementNum) :

		cullentE = elementList[i]
		dprint(str(i)+": "+cullentE+","+ansString)
		nowLen = len(ansString)
			
		if len(ansString) > 0 :
			previousE = ansString[-1]
		else :
			previousE = "-"


		# combine可能かチェック
		if previousE in combineRule[cullentE] :

			dprint("combine")
			# 回答作成
			ansString = ansString[:-1] + combineRule[cullentE][previousE]

			# 前述のがelasePlaceに追加されていないかチェック
			for char in elasePlace :
				for j in xrange(len(elasePlace[char])) :
					if elasePlace[char][j] >= nowLen-1 :
						del elasePlace[char][j]

		# opposedの組み合わせが完成するかチェック
		elif len(elasePlace[cullentE])>0 :
			dprint("del")

			deleteStartNum = 0
			#deleteStartNum = elasePlace[cullentE][-1]
			
			# 回答作成
			ansString = ''
			#ansString = ansString[:deleteStartNum]

			# 余分なdeletePlaceを削除
			for char in elasePlace :
				elasePlace[char] = []
				#for j in xrange(len(elasePlace[char])) :
					#if elasePlace[char][j] >= deleteStartNum :
						#del elasePlace[char][j]

		# 削除に成りうるかチェック
		elif len(opposedRule[cullentE])>0 :
			dprint("AddOpposed")


			for opposedE in opposedRule[cullentE] :
				elasePlace[opposedE].append(nowLen)

			ansString = ansString + cullentE

		# 何事もない
		else :
			dprint("NoneEvent")

			ansString = ansString + cullentE

		dprint(ansString)
		dprint(elasePlace)

	dprint(ansString)
	PrintAArrayWithKakko(q,[c for c in ansString])
	
