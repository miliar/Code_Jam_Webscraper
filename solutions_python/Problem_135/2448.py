#!/usr/bin/python

f = file("A-small-attempt4.in")
fo = file("a.out", "w")
n = f.readline()

for i in range(int(n)):
	check1 = []
	n1 = int(f.readline())
	for j in range(4):
		if (n1-1) == j:
			check1 = f.readline().split()
		else:
			f.readline()
	check2 = []
	n2 = int(f.readline())
	for j in range(4):
		if (n2-1) == j:
			check2 = f.readline().split()
		else:
			f.readline()
	r = []
	for k in range(len(check1)):
		if check1[k] in check2:
			r.append(check1[k])

	af = "\n"
	if i == int(n)-1:
		af = ""
	if(len(r) < 1):
		fo.write("Case #"+str(i+1)+": Volunteer cheated!" + af)
	elif(1 < len(r)):
		fo.write("Case #"+str(i+1)+": Bad magician!" + af)
	else:
		fo.write("Case #"+str(i+1)+": " + r[0] + af)
f.close()
fo.close()
