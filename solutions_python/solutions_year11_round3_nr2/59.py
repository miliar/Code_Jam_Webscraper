# -*- coding: utf-8 -*-
import sys

# 一行読む
def ReadL():
	return sys.stdin.readline()[0:-1]

# 一行読んでINTにする
def ReadLInt():
	return int(ReadL())


# スペースで区切って一行読む
def ReadLSplit():
	return ReadL().split(' ')

# さらにINT型にする
def ReadLSplitInt():
	return [int(x) for x in ReadLSplit()]

# 回答を出力する
def PrintA(q,out):
	print 'Case #'+str(q+1)+': '+str(out)

# 回答を出力する
def PrintAArray(q,array):
	st = ''
	for s in array:
		st += str(s) + ' '
	PrintA(q,st)

# 回答を出力する
def PrintAArrayWithKakko(q,array):
	st = ''

	if len (array)== 0 :
		PrintA(q,'[]')
		return

	for s in array:
		st += str(s) + ', '
	PrintA(q,'['+st[:-2]+']')

# 標準エラー出力
def ShowEr(value):
	sys.stderr.write(str(value)+"\n")

# 問題番号出力
def ShowQueNum(q):
	ShowEr("---question:"+str(q+1)+"---")

# 簡単出力
def ShowData(name,d):
	ShowEr(str(name)+" :"+str(d))

# 簡単列出力 
def ShowListData(name,d):
	out = ""
	for o in d:
		out +=","+str(o)
	ShowData(name,out[1:])

# 括弧付き列出力
def ShowKakkoTsukiListData(name,alist):
	out = "["
	for o in alist :
		out +=","+str(o)		

qNum = ReadLInt()

debugMode = False

def dprint(str):
	if debugMode :
		print str


for q in xrange(qNum):
	
	line = ReadLSplitInt()

	bNum = line[0]

	bTime = line[1]

	sNum = line[2]

	kuriNum = line[3]

	kuri = line[4:]

	dprint(kuri)


	a = int(sNum / kuriNum)
	b = sNum - (a*kuriNum)

	kaisu = []
	aLoopM = 0
	nonBoostTotalM = 0

	for i in xrange(kuriNum):
		aLoopM += kuri[i]
		if a*kuriNum == sNum :
			kaisu.append(a)
		elif i < b :
			kaisu.append(a+1)
		else :
			kaisu.append(a)
		nonBoostTotalM+=kaisu[i]*kuri[i]

	nowTime = 0
	# Boosterが出来るまで進む
	loopCount = int(bTime / (aLoopM*2))
	nokoriMakeTime = bTime - aLoopM*2*loopCount

	dprint(loopCount)
	dprint(nokoriMakeTime)

	for i in xrange(kuriNum) :
		kaisu[i]-=loopCount
		kuri[i] = float(kuri[i])

	for i in xrange(kuriNum) :
		if kuri[i]*2 <= nokoriMakeTime :
			nokoriMakeTime -=kuri[i]*2
			kaisu[i]-=1
		else :
			kaisu[i]-=1
			nokorikyori = kuri[i] - ( float(nokoriMakeTime)/2 )
			kuri.append(nokorikyori)
			kaisu.append(1)
			kuriNum+=1
			break
	dprint(kuri)
	dprint(kaisu)

	breakFlag = True

	totalTime = nonBoostTotalM*2
	nokoriBooster = bNum

	if bTime >= nonBoostTotalM :
		PrintA(q,totalTime)
		continue

	dprint("time:"+str(totalTime))
	while breakFlag :

		#ブースト切れ
		if nokoriBooster == 0 :
			break

		#最大時間を探す
		maxI = 0
		maxM = float(0)
		for i in xrange(kuriNum) :
			if kaisu[i]!=0 and maxM < kuri[i] :
				maxM = kuri[i]
				maxI = i
		dprint("max:"+str(maxM))
		#最大時間ブースとする
		if kaisu[maxI] <= nokoriBooster :
			totalTime-=kuri[maxI]*kaisu[maxI]
			nokoriBooster-=kaisu[maxI]
			kaisu[maxI]=0
			dprint("allBooster")
			dprint(kuri[maxI]*kaisu[maxI])
		else :
			totalTime-=nokoriBooster*kuri[maxI]
			kaisu[maxI]-=nokoriBooster
			nokoriBooster=0
			dprint("zanBooster")
		dprint("time:"+str(totalTime))
	#nokoriBoostMakeTime = loopCount*aLoopM


	dprint(totalTime)
	dprint(kaisu)

	PrintA(q,int(totalTime))
	
	

