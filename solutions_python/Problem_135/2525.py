# encoding=UTF-8
import os
data = open('A-small-attempt1.in','r')
res = open('res.txt','w')
T = int(data.readline())
for s in range(T):
	first_r = int(data.readline())
	row1=['' for i in range(4)]
	row2=['' for i in range(4)]
	for i in range(4):
		line = data.readline()
		if i == first_r-1:
			row1 = line.split()
	second_r = int(data.readline())
	for i in range(4):
		line = data.readline()
		if i == second_r-1:
			row2 = line.split()
	result=[]
	for i in range(4):
		for j in range(4):
			if row1[i] == row2[j]:
				result.append(row1[i])
	res.write('Case #'+str(s+1)+': ')
	if len(result) == 1:
		res.write(result[0]+'\n')
	elif len(result) == 0:
		res.write('Volunteer cheated!\n')
	else:
		res.write('Bad magician!\n')
data.close()
res.close()
