#!/usr/bin/python

f = open('A-small-attempt0.in')
#f = open('A-small-input0.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('magic_small.txt', 'w')



for i in range (1,numcase+1):
	inputline = f.readline()
	firstnum = int(inputline)
	#print "i="+str(i)+" firstnum="+str(firstnum)
	for j in range(1,5):
		inputline = f.readline()
		#print "  line no="+str(j)
		if j == firstnum:
			linelist = inputline.split()
			firstrow = []
			for k in range (0,4):
				firstrow.append(int(linelist[k]))
	inputline = f.readline()
	#print "#line="+inputline
	secondnum = int(inputline)
	for j in range(1,5):
		inputline = f.readline()
		if j == secondnum:
			linelist = inputline.split()
			secondrow = []
			for k in range (0,4):
				secondrow.append(int(linelist[k]))
	candidates = []
	for j in range(0,4):
		possnum = firstrow[j]
		for k in range(0,4):
			if possnum == secondrow[k]:
				candidates.append(possnum)
	if len(candidates) == 1:
		answer_out = "Case #"+str(i)+": "+str(candidates[0])+"\n"
	elif len(candidates) == 0:
		answer_out =  "Case #"+str(i)+": "+"Volunteer cheated!"+"\n"
	else:
		answer_out = "Case #"+str(i)+": "+"Bad magician!"+"\n"
	fout.write(answer_out)
	print answer_out