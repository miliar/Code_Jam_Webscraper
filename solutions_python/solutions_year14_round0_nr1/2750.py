#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

f = open('A-small-attempt0.in','r')
s = open('sorti.txt','w')
n = int(f.readline())
i=1

if n>=1 and n<=100:
	while i<=n:
		val1 = int(f.readline())
		k=1
		while k<=4:
			if k == val1:
				ligne1 = f.readline().rstrip('\n\r')
				ligne1 = ligne1.split(" ")
			else:
				f.readline()
			k+=1
		k=1
		val2 = int(f.readline())
		while k<=4:
			if k == val2:
				ligne2 = f.readline().rstrip('\n\r')
				ligne2 = ligne2.split(" ")
			else:
				f.readline()
			k+=1

		cpt = 0
		elm = 0
		for el in ligne1:
			if el in ligne2:
				cpt += 1
				elm = int(el)
		if cpt == 0:
			var = "Case #"+str(i)+": Volunteer cheated!\n"
		elif cpt == 1:
			var ="Case #"+str(i)+": "+str(elm)+"\n"
		elif cpt:
			var = "Case #"+str(i)+": Bad magician!\n"
		s.write(var)
		i+=1
