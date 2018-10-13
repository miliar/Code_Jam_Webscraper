import sys
import os


def checkGrass(grass):
	res="YES"

	if len(grass) == 1 or len(grass[0]) == 1:
		return res
	
	for i in range(len(grass)):
		for j in range(len(grass[i])):
		
			has1 = True
			for z in range(len(grass)):
				if grass[z][j] <= grass[i][j]:
					continue
				else:
					has1 = False
					break
			
			has2 = True
			for z in range(len(grass[i])):
				if grass[i][z] <= grass[i][j]:
					continue
				else:
					has2 = False
					break
			
			if not has1 and not has2:
				res = "NO"
				return res

	return res



inp = ""


with open('b1.out', 'w') as fo:

	with open(sys.argv[1], 'r') as fi:
		caseno = int(fi.readline())

		for i in range(caseno):
			grass = []
			linec = int((fi.readline().strip().split(" "))[0])
				
			for j in range(linec):
				ln = fi.readline().strip().split(" ")
				for z in range(len(ln)):
					ln[z] = int(ln[z])
				grass.append(ln)

			fo.write("Case #"+str(i+1)+": "+checkGrass(grass)+"\n")
			
		fi.closed

	fo.closed






