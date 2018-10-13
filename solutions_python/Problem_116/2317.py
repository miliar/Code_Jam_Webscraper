#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

def evaluate(checkBoard, cntr):
	#print checkBoard
	rlist = []
	clist = []
	dlist = [[],[]]
	dotr = 0
	dotc = 0
	dotd = 0
	for i in range(0,4):
		rlist.append(list(checkBoard[5*i:5*i+4]))
		clist.append([checkBoard[0+i],checkBoard[5+i],checkBoard[10+i],checkBoard[15+i]])
	
	for i in range(0,4):
		dlist[0].append(checkBoard[6*i])
		dlist[1].append(checkBoard[(i+1)*4-1])
	
	for lstr,lstc in zip(rlist,clist):
		if sorted(lstr) in [['T','X','X','X'],['X','X','X','X']] or sorted(lstc) in [['T','X','X','X'],['X','X','X','X']]:
			return("Case #"+str(cntr)+": X won")
		elif sorted(lstr) in [['O','O','O','T'],['O','O','O','O']] or sorted(lstc) in [['O','O','O','T'],['O','O','O','O']]:
			return("Case #"+str(cntr)+": O won")
		if '.' in lstr:
			dotr += 1
		if '.' in lstc:
			dotc += 1
		
	for lst in dlist:
		if sorted(lst) in [['T','X','X','X'],['X','X','X','X']]:
			return("Case #"+str(cntr)+": X won")
		elif sorted(lst) in [['O','O','O','T'],['O','O','O','O']]:
			return("Case #"+str(cntr)+": O won")
		if '.' in lst:
			dotd += 1
	
	if dotr==0 and dotc==0 and dotd==0:
		return ("Case #"+str(cntr)+": Draw")
	return("Case #"+str(cntr)+": Game has not completed")
	
	
			
	

def main():
	checkBoard = []
	cntr = 0
	f = open("A-large.in")
	count = int(f.readline())
	
	for line in f:
		
		if line != '\n':
			checkBoard += line
		else:
			cntr += 1
			print evaluate(checkBoard, cntr)
			checkBoard = []
	return 0

if __name__ == '__main__':
	main()
