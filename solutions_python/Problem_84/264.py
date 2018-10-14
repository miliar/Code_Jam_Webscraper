#!/usr/bin/python

blue = []
red = []
#white = []

def ispossible(x,y):
	global blue,red
#	try:
#		print '>',(x>=0) and (y>=0)
#		print (y+1 <len(blue)) 
#		print (len(blue[y])>x+1) 
#		print (blue[y][x]=='#' or blue[y][x+1]=='#' or blue[y+1][x]=='#' or blue[y+1][x+1]=='#') 
#		print '<',(red[y][x]==' ' and red[y][x+1]==' ' and red[y+1][x]==' ' and red[y+1][x+1]==' ')
#	except:
#		None
	
	return (x>=0) and (y>=0) \
		and (y+1<len(blue)) \
		and (len(blue[y])>x+1) \
		and (blue[y][x]=='#' and blue[y][x+1]=='#' and blue[y+1][x]=='#' and blue[y+1][x+1]=='#') \
		and (red[y][x]==' ' and red[y][x+1]==' ' and red[y+1][x]==' ' and red[y+1][x+1]==' ')

def mark(x,y, c):
	global red, blue
	if (c=='@'):
		red[y] = red[y][:x] + "/\\" + red[y][x+2:]
		red[y+1] = red[y+1][:x] + "\\/" + red[y+1][x+2:]
	else:
		red[y] = red[y][:x] + "  " + red[y][x+2:]      	
		red[y+1] = red[y+1][:x] + "  " + red[y+1][x+2:]
	
#		for x in range(bx,bx+2):
#			red[y][x] = c


def dotest(x,y):
	global red, blue
	if y>=len(blue):
		return True
	nx = x+1
	ny = y
	if (nx>=len(blue[0])):
		nx = 0
		ny = ny+1
	if ispossible(x,y):
#		print "possible",x,y
		mark(x,y,'@')
		if dotest(nx,ny):
			return True
		mark(x,y,' ')
		if blue[y][x]=='#':
			return False
		return dotest(nx,ny)
	else:
#		print x,y
#		print blue[y]
		if blue[y][x]=='#' and red[y][x]==' ':
			return False
	return dotest(nx,ny)

def display():
	import sys
	global red,blue
	ln = 0
	for line in red:
		for i in range(len(line)):
			if blue[ln][i]=='.':
				sys.stdout.write(blue[ln][i])
			else:
				sys.stdout.write(line[i])
		print ""
		ln = ln+1

import sys
sys.setrecursionlimit(100000)

TESTCASES = input()
for tcase in range(1,TESTCASES+1):
	sy = input()
	sx = input()
	blue = []
	red = []
#	print tcase, sy, sx
	blue = [raw_input() for l in range(sy)]
	red = [' '*sx for l in range(sy)]
	print "Case #%d:"%tcase
#	print blue
#	print red
#	if dotest(0,0):
	if dotest(0,0):
		display()
	else:
		print "Impossible"
#	for l in range(sy):
#		line = raw_input()
#		blue[l] = line
#		print 'line:', line
