#!/usr/bin/python
def main():
	fin = open("./data2.in", "r")
	fout = open("./output2.txt", "w")

	firstline = 0
	counts = 0
	for line in fin:
		if firstline != 0:
			test = (firstline -1)  % 3
			 
			if test == 0:
				nblocks = []
				kblocks = []
			elif test == 1:
				line = line.split()
				nblocks = [float(i) for i in line] 
			else:
				counts += 1
				line = line.split()
				kblocks = [float(i) for i in line]	
				DWar(list(nblocks), list(kblocks))
				fout.write("Case #" + str(counts) + ": " +  DWar(list(nblocks), list(kblocks)) + " " +  WarFair(list(nblocks), list(kblocks)) + "\n")
		firstline += 1


def DWar(n, k):
	n.sort()
	k.sort()
#	n = n[::-1]
#	k = k[::-1]
	
	wins = 0
	while (n != []):
		i = 0
		
		if n[0] > k[0]:
			wins += 1
			i = 0
		else:
			i = -1
		del n[0]
		del k[i]

	return str(wins)

def WarFair(n, k):
	n.sort()
	k.sort()
	wins = 0
	i = 0
	while(n != []): 
		i = 0	
		for e in k:
			if e > n[0]:
				break
			else:
				i += 1
		if i == len(k):
			i = 0
			wins += 1
		del n[0]
		del k[i]

	return str(wins)
main()

