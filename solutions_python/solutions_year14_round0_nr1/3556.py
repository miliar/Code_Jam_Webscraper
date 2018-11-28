#!/usr/bin/python
import sys

def intersect(a, b):
     return list(set(a) & set(b))

al = open(sys.argv[1],'r').read().splitlines()
nb_cases = int(al[0])

def oracle(links):
	print(links)
i=1
for n in range(nb_cases):
	range1=int(al[1])
	square1=al[2:6]
	range2=int(al[6])
	square2=al[7:11]
	try:
		x = intersect(square1[range1-1].split(" "), square2[range2-1].split(" "))
	except:
		print(range1, square1, range2, square2)
		exit(1)
	if len(x)==1:
		print("Case #%s: %s"%(i,x[0]))
	elif len(x)>1:
		print("Case #%s: Bad magician!"%i)
	else:
		print("Case #%s: Volunteer cheated!"%i)
	al=[al[0]]+al[11:]
	i=i+1

