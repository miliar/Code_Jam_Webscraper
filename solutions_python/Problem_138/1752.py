#!/usr/bin/python

fin = open('deceit-sample.txt')
fin = open('D-large.in')
inputline = fin.readline()
numcase = int(inputline)

fout = open('deceit_large_result.txt', 'w')


def pickpiece(list, piece):
	templist = []
	for i in range(0,len(list)):
		if list[i] > piece:
			templist.append(list[i])
	if len(templist) == 0:
		return -1
	else:
		return min(templist)

for i in range (1,numcase+1):
	line = fin.readline()
	numblock = int(line)
	line = fin.readline()
	linelist = line.split()
	naomi = []
	naomid = []
	for j in range (0,numblock):
		naomi.append(float(linelist[j]))
		naomid.append(float(linelist[j]))
	line = fin.readline()
	linelist = line.split()
	ken = []
	kend = []
	for j in range (0,numblock):
		ken.append(float(linelist[j]))
		kend.append(float(linelist[j]))
	deceit = 0
	for j in range (0,numblock):
		pk = kend[j]
		pn = pickpiece(naomid,pk)
		if pn != -1:
			deceit += 1
			naomid.remove(pn)
	war = 0
	for j in range (0,numblock):
		pn = naomi[j]
		pk = pickpiece(ken, pn)
		if pk == -1:
			war += 1
		else:
			ken.remove(pk)
	answer_out = "Case #"+str(i)+": "+str(deceit)+" "+str(war)+"\n"
	fout.write(answer_out)
	print answer_out