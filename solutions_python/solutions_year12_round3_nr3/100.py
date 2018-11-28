# -*- coding: utf-8 -*-
import sys
import math

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

# さらにINT型にする
def ReadLSplitFloat():
	return [float(x) for x in ReadLSplit()]

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
#debugMode = True

def dprint(str):
	if debugMode :
		print str

def solve( boxs,toys,boxCB,toyCB,boxTB,toyTB,boxNB,toyNB,countB ):

	ans1 = countB
	ans2 = countB
	dprint( "(" + str(boxCB) + "," + str(toyCB) + "): " + str(countB) );
	if boxCB != len(boxs) :
		boxN = boxs[boxCB][0]
		boxT = boxs[boxCB][1]
		boxC = boxCB + 1
		toyN = toyNB
		toyT = toyTB
		toyC = toyCB
		count = countB
		
		if toyT == boxT :
			if toyN > boxN :
				count = countB + boxN
				toyN = toyN - boxN
				boxN = 0
			else :
				count = countB + toyN
				boxN = boxN - toyN
				toyN = 0

		ans1 = solve( boxs,toys,boxC,toyC,boxT,toyT,boxN,toyN,count )
	if toyCB != len(toys) :
		toyN = toys[toyCB][0]
		toyT = toys[toyCB][1]
		toyC = toyCB + 1
		boxN = boxNB
		boxT = boxTB
		boxC = boxCB
		count = countB
		
		if toyT == boxT :
			if toyN > boxN :
				count = countB + boxN
				toyN = toyN - boxN
				boxN = 0
			else :
				count = countB + toyN
				boxN = boxN - toyN
				toyN = 0

		ans2 = solve( boxs,toys,boxC,toyC,boxT,toyT,boxN,toyN,count )

	if ans1 > ans2 :
		return ans1
	else :
		return ans2
	
for q in xrange(qNum):
	
	( boxNum , toyNum ) = ReadLSplitInt()
	
	boxline = ReadLSplitInt()
	toyline = ReadLSplitInt()
	boxs = []
	toys = []
	for i in xrange(boxNum) :
		boxs.append( [ boxline[i*2] , boxline[i*2+1] ] )
	for i in xrange(toyNum) :
		toys.append( [ toyline[i*2] , toyline[i*2+1] ] )

	dprint( boxs )
	dprint( toys )
	
	boxT = boxs[0][1]
	boxN = boxs[0][0]
	toyT = toys[0][1]
	toyN = toys[0][0]
	count = 0

	if toyT == boxT :
		if toyN > boxN :
			count = count + boxN
			toyN = toyN - boxN
			boxN = 0
		else :
			count = count + toyN
			boxN = boxN - toyN
			toyN = 0
	ans = solve( boxs,toys,1,1,boxT,toyT,boxN,toyN,count )

	PrintA( q , ans )

