#!/usr/bin/python

def inp():
	fin=file('inp.txt','r')
	fout=file('out.txt','a')
	totcase=fin.readline()
	for move in range(int(totcase)):
		num=fin.readline()
		case=fin.readline()
		result=compute(num,case)
		out(fout,move,result)

def compute(num,case):
	candylist=case.split(" ")
	elem=xor(candylist)
	if elem!=0:
		result="NO"
		return result
	result=minim(candylist,num)
	return result

def xor(candylist):
	elem=0
	for move in candylist:
		elem=elem^int(move)
	return elem

def minim(candylist,num):
	minim=int(candylist.pop(0))
	result=int(minim)
	for move in range(int(num)-1):
		elem=candylist.pop(0)
		result=result+int(elem)
		if int(elem)<int(minim):
			minim=elem
	result=result-int(minim)
	return result

def out(fout,move,result):
	fout.write("Case #" + str(move+1) + ": " + str(result) +'\n')

def main():
	inp()

main()
