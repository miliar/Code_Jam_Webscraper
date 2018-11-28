#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys
def fuckFuntion(case,O,B):
	t = 0
	posO = 1
	posB = 1
	end = False
	make = False
	while not end:
		t = t +1
		if not O==[]:
			if posO > int(O[0]):
				posO = posO - 1
			elif posO < int(O[0]):
				posO = posO + 1
			else:
				if case[0]== "O"+str(posO):
					make = True
					O.pop(0)
		if not B==[]:
			if posB > int(B[0]):
				posB = posB - 1
			elif posB < int(B[0]):
				posB = posB + 1
			else:
				if case[0] == "B"+str(posB):
					make = True
					B.pop(0)
		if make==True:
			case.pop(0)
			if case==[]:
				end=True
			make=False
	return t

if __name__ == "__main__":
	f=open(sys.argv[1],"r")
	cases = f.readlines()[1:]
	for case in cases:
		index = cases.index(case)
		case = case[:len(case)-1].split(" ")
		O = []
		B = []
		for i in range(int(case.pop(0))):
			meme = case.pop(i)+case.pop(i)
			case.insert(i,meme)
			if case[i][0]=="B":
				B = B+[case[i][1:]]
			if case[i][0]=="O":
				O = O+[case[i][1:]]
		print "Case #"+str(index+1)+": " + str(fuckFuntion(case,O,B))
