#!/usr/bin/python3
import sys

def prin(s):
	print(s, end="")

def nextline():
	return inf.readline().strip()

if len(sys.argv) != 2:
	sys.exit("Usage: "+sys.argv[0]+" inputfilename")
	
infilename=sys.argv[1]
inf=open(infilename,'r')

T=int(nextline())
for case in range(0,T):
	prin("Case #" + str(case+1) + ": ")
#	print()
	row1=[]
	row2=[]
	line=nextline()
	ans1=int(line)-1
	for i in range(0,4):
		line=nextline()
		row1.insert(i, line.split(" "))
	line=nextline()
	ans2=int(line)-1
	for i in range(0,4):
		line=nextline()
		row2.insert(i, line.split(" "))
	selectedCard=[]
	for i in range(0,4):
#		print(row1[ans1][i])
#		print(row2[ans2])
		if row1[ans1][i] in row2[ans2]:
			selectedCard.append(row1[ans1][i])
#	for i in selectedCard:
#		print(i)
	if len(selectedCard) < 1:
		print("Volunteer cheated!")
	elif len(selectedCard) == 1:
		print(selectedCard[0])
	else:
		print("Bad magician!");
#	print("ans1="+str(ans1))
#	for i in range(0,4):
#		for j in range(0,4):
#			prin(row1[i][j])
#			prin(" ")
#		print()
#	print("ans2="+str(ans2))
#	for i in range(0,4):
#		for j in range(0,4):
#			prin(row2[i][j])
#			prin(" ")
#		print()
inf.close()
