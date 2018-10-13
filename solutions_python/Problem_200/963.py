#!/usr/bin/python3

import sys

def IntToDec( num ):
	res = []
	while num != 0:
		res = res + [num%10]
		num = num//10
	res.reverse()
	return res

def DecToInt( arr ):
	res = 0
	for i in arr:
		res = res * 10 + i;
	return res

def getNonIncDigit( arr ):
	start = 0;
	cnt = 0
	for i in arr:
#		print(i)
		if i < start:
#			print('i%d s%d'%(i,start))
			return cnt
		start = i
		cnt = cnt + 1
	return -1

def GetPrevTidyNum( num ):
	while True:
		arr = IntToDec(num)
		odigit = getNonIncDigit(arr)
		if odigit == -1:
			return num
		for i in range(odigit,len(arr)):
			arr[i] = 0
		num = DecToInt(arr)
		num = num - 1

inputbuff = ''
def clearInputWhiteSpace():
	global inputbuff
	while True:
		if len(inputbuff) == 0:
			break
		if not (inputbuff[0] == ' ' or inputbuff[0] == '\n' or inputbuff[0] == ' '):
			break
		
		inputbuff = inputbuff[1:]

def readint():
	global inputbuff
	while True:
		clearInputWhiteSpace();
		inputbuff = inputbuff.replace('\n', ' ')
		inputbuff = inputbuff.replace('\r', ' ')
		clearInputWhiteSpace();
		
		csp = inputbuff.split(' ')
		if len(csp) < 2:
			inputbuff = inputbuff + sys.stdin.readline()
			continue
		else:
			inputbuff = ' '.join(csp[1:])
#			print('Got %d'%int(csp[0]))
			return int(csp[0])

def mainfunc():
	casecnt = readint()
	for i in range(casecnt):
		currval = readint()
		res = GetPrevTidyNum(currval)
		print( 'Case #%d: %d'%(i+1, res) )

mainfunc()
