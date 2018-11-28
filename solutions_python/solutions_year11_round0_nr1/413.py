#!/usr/bin/python

def inp():
	fout=file('out.txt', 'a')
	fin=file('inp.txt', 'r')
	testCases=fin.readline()
	for count in range(int(testCases)):
		case=fin.readline()
		result=compute(case)
		out(result, count, fout)

def compute(case):
	clist=case.split(" ")
	num=clist.pop(0)
	color="N"
	olist=[]
	blist=[]
	mlist=[]
	for move in clist:
		if color=="N":
			color=move
			mlist.append(move)
		elif color=="O":
			olist.append(move)
			color="N"
		elif color=="B":
			blist.append(move)
			color="N"
	ocurr=bcurr=1
	onext=bnext=1
	if olist:
		onext=olist.pop(0)
	if blist:
		bnext=blist.pop(0)
	result=0
	for button in mlist:
		omoves=int(onext)-int(ocurr)
		bmoves=int(bnext)-int(bcurr)	
		if button=="O":
			result=result+mod(omoves)+1
			ocurr=onext
			if mod(omoves)+1>mod(bmoves):
				bcurr=bnext
			else:
				bcurr=int(bcurr)+((bmoves/mod(bmoves))*(mod(omoves)+1))
			if olist:
				onext=olist.pop(0)
		else:
			result=result+mod(bmoves)+1
			bcurr=bnext
			if mod(bmoves)+1>mod(omoves):
				ocurr=onext
			else:
				ocurr=int(ocurr)+((omoves/mod(omoves))*(mod(bmoves)+1))
			if blist:
				bnext=blist.pop(0)	
	return result

def mod(numb):
	if numb>0:
		return numb
	else:
		return -numb

def out(result, count, fout):
	fout.write("Case #" + str(count+1) + ": " + str(result)+ '\n')

def main():
	inp()

main()
