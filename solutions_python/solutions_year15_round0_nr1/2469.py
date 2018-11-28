#!/usr/bin/env python
fin = open('A-large.in')
fout = open('output-large', 'w')

ncase = int(fin.readline())

for i in range(ncase):
	line = fin.readline().split()
	audiences=[]
	total=[0]
	requires=0
	for audience in line[1]:
		if audience != '\n':
			audiences.append(int(audience))
	for j in range(1,len(audiences)):
		while  (total[j-1] + audiences[j-1]) < j:
			total[j-1] += 1
			requires += 1
		total.append(total[j-1] + audiences[j-1])

	fout.write("Case #{0}: {1}\n".format(i+1,requires))

fin.close()
fout.close()
