#! /Library/Frameworks/Python.framework/Versions/2.6/bin/python

import itertools

f=open("inpfile","r")
f.readline()
count=0
for line in f.readlines():
	num = line.strip("\n")
	digits=len(num)
	combinations1=[]

	for combination in itertools.permutations(num,digits):
 		combinations1.append(str("".join(str(i) for i in combination)))


	newlist=[]
	for x in combinations1:
		if x not in newlist:
			newlist.append(str(x))
	
	newlist1 = sorted(newlist)
	ind = newlist1.index(num)
	if ind+1 == len(newlist):
		out = str(newlist1[0])
		temp=1
		while (out[0] == "0"):
			out = str(newlist1[temp])
			temp=temp+1

		out1 = out[0:1]+"0"+out[1:]
	else:
		out1 = str(newlist1[ind+1])
	
	count=count+1
	print "Case #" + str(count) + ": " + out1

