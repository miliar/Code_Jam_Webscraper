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
	
	lines = ReadLSplitInt()
	
	yoko = lines[1]
	tate = lines[0]
	
	matrix = []

	for x in xrange(tate) :

		code=ReadL()
		line = []
		for y in xrange(yoko) :

			line.append(code[y])
		matrix.append(line)

	breaksign = False

	for x in xrange(tate) :
		for y in xrange(yoko) :

			moji = matrix[x][y]
			
			if moji == "#" :
				if x == tate-1 or y == yoko-1 :
					breaksign = True
					break
				if matrix[x+1][y] == "#" and matrix[x][y+1]=="#" and matrix[x+1][y+1]=="#" :
					matrix[x][y]="/"
					matrix[x+1][y]="\\"
					matrix[x][y+1]="\\"
					matrix[x+1][y+1]="/"
				else :
					breaksign = True
					break
		if breaksign :
			break
				

	print "Case #"+str(q+1)+":"

	if breaksign :
		print "Impossible"
	else :
		
		dprint(matrix)
		for x in xrange(tate) :
			line = ""
			for y in xrange(yoko) :
				line += matrix[x][y]

			print line
				
	


