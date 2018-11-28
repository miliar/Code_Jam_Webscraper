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
	
	nagasa = ReadLInt()

	matrix = []

	for i in xrange(nagasa) :
		
		gyou = []

		line = ReadL()

		for j in xrange(nagasa) :

			gyou.append(line[j])
		
		matrix.append(gyou)


	dprint(matrix)
		
	WP = []

	for player in xrange(nagasa):
		
		winNum = 0
		shiaiNum = 0

		for i in xrange(nagasa):

			if matrix[player][i] == "1" :
				winNum+=1 
				shiaiNum+=1 
			elif matrix[player][i] == "0" :
				shiaiNum+=1


		WP.append(float(winNum)/shiaiNum)

	dprint(WP)

	OWP = []
	
	for player in xrange(nagasa):
		
		winNum = float(0)
		shiaiNum = 0

		for i in xrange(nagasa):

			if matrix[player][i] != "." :

				winNum2=0
				shiaiNum2=0
				for j in xrange(nagasa) :
					if matrix[i][j] == "1" and j != player :
						winNum2+=1
						shiaiNum2+=1
					if matrix[i][j] == "0" and j != player :
						shiaiNum2+=1

				winNum+=float(winNum2)/shiaiNum2
				shiaiNum+=1 


		OWP.append(float(winNum)/float(shiaiNum))
	dprint(OWP)
	
	OOWP = []

	for player in xrange(nagasa):
		
		winNum = float(0)
		shiaiNum = 0

		for i in xrange(nagasa):

			if matrix[player][i] != "." :
				winNum+=OWP[i] 
				shiaiNum+=1 

		OOWP.append(float(winNum)/float(shiaiNum))
	dprint(OOWP)

	print "Case #"+str(q+1)+":"

	for i in xrange(nagasa) :

		RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]		

		print RPI


