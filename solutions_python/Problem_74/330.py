#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gjam import *

qNum = ReadLInt()

debugMode = False

def dprint(str):
	if debugMode :
		print str

def distance(place1,place2):
	if place1 > place2 :
		return place1 - place2
	else :
		return place2 - place1
def GetAnotherRobot( robot ):
	if robot == 'O' :
		return 'B'
	else :
		return 'O'

for q in xrange(qNum):

	items = ReadLSplit()
	pushNum = int(items[0])

	#if q != 1 :
		#continue
	# [ O or B , Number , NextNumber ]

	previousOrangeI = -1
	previousBlueI = -1

	del(items[0])

	pushList = []
	previousPushI = { 'O' : -1 , 'B' : -1 }
	firstPush = { 'O' : -1 , 'B' : -1 }

	for i in xrange(pushNum) :

		robot = items[i*2]
		button = int(items[i*2+1])
		
		pushSheet = [ robot , button , -1 ]
		pushList.append(pushSheet)

		# 最初のボタンを見つける
		if firstPush[ robot ] == -1 :
			firstPush[ robot ] = button

		# 次のボタンをセット
		if previousPushI[ robot ] != -1 :
			pushList[ previousPushI[robot] ][2] = button

		previousPushI[ robot ] = i
		
	#print firstPush
	

	nokoriHosu = { 'O' : -1 , 'B' : -1 }
	nokoriHosu = { 
			'O' : distance(firstPush['O'],1) ,
			'B' : distance(firstPush['B'],1) }
	targetButton = {
			'O' : firstPush['O'] ,
			'B' : firstPush['B'] }

	totalTime = 0

	dprint(nokoriHosu)
	for i in xrange(pushNum) :

		dprint('-- '+str(i)+' --')  

		pushSheet = pushList[i]

		robot = pushSheet[0]
		button = pushSheet[1]
		nextbutton = pushSheet[2]
		anotherRobot = GetAnotherRobot(robot)

		dprint(pushSheet)

		# 移動時間
		moveTime = nokoriHosu[robot]

		# 移動時間＋押す時間を加算
		totalTime += moveTime+1

		# 次のターゲットへの残り歩数を求める
		if nextbutton != -1 :
			nokoriHosu[robot] = distance(button,nextbutton)
		else :
			nokoriHosu[robot] = -1

		# もう片方のロボットを動かす
		if nokoriHosu[anotherRobot] > 0 :
			hosu = nokoriHosu[anotherRobot] - (moveTime+1)
			if hosu < 0 :
				nokoriHosu[anotherRobot] = 0
			else :
				nokoriHosu[anotherRobot] = hosu
		dprint(nokoriHosu)
	PrintA(q,totalTime)

	

