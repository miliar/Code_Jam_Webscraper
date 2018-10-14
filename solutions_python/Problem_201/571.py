# -*- coding: utf-8 -*-
# @Author: Patrice Béchard 20019173
# @Date:   2017-04-07 22:21:40
# @Last Modified time: 2017-04-08 13:17:20
#
# bathroom stalls
# 

####
#list of tuples method

file = 'input.txt'
file = 'C-large.in'
file2 = 'output2.txt'
f = open(file)
g = open(file2,'w')

nCase = int(f.readline().strip())

for i in range(nCase):
	print(i)
	temp = f.readline().strip().split()
	nStalls = int(temp[0])
	nUsers = int(temp[1])
	gaps = [[1,nStalls]]
	j = 0
	while j < nUsers-gaps[0][0]:
		if gaps[0][1]%2 == 0:						#even
			max1 = gaps[0][1]//2
			max2 = gaps[0][1]//2 - 1
			in1,in2 = False,False
			for k in range(len(gaps)):
				if gaps[k][1] == max1:
					gaps[k][0] += gaps[0][0]
					in1 = True
				if gaps[k][1] == max2:
					gaps[k][0] += gaps[0][0]
					in2 = True
			if not in1:
				gaps.append([gaps[0][0],max1])
			if not in2:
				gaps.append([gaps[0][0],max2])
		else:										#odd
			max1 = gaps[0][1]//2
			in1 = False
			for k in range(len(gaps)):
				if gaps[k][1] == max1:
					gaps[k][0] += 2*gaps[0][0]
					in1 = True
			if not in1:
				gaps.append([2*gaps[0][0],max1])
		j += gaps[0][0]
		del gaps[0]

	maximum = gaps[0][1]
	if maximum%2 == 0:
		Ls,Rs = maximum//2-1,maximum//2
	else: 
		Ls,Rs = maximum//2,maximum//2
	g.write("Case #%d: %d %d\n"%(i+1,max(Ls,Rs),min(Ls,Rs)))
