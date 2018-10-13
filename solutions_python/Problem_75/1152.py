#!/usr/bin/python

inp = "B-large.in"
out = "B-large.out"
lis = list(map(str.rstrip, open(inp, 'r').readlines()))
cases = int(lis[0])
lis = lis[1:]
for i in range(cases):
	combtrans = {}
	ertrans = []
	a = int(lis[i].split()[0])
	for j in range(a):
		combtrans[lis[i].split()[j+1][:2]] = lis[i].split()[j+1][2]
		combtrans[''.join(list(reversed(lis[i].split()[j+1][:2])))] = lis[i].split()[j+1][2]
	for j in range(int(lis[i].split()[a+1])):
		ertrans.append(lis[i].split()[j+a+2][:2])
		ertrans.append(''.join(list(reversed(lis[i].split()[j+a+2][:2]))))
	z = list(lis[i].split()[int(lis[i].split()[a+1])+a+3])
	b = []
	b.append(z[0])
	for x in (range(1,len(z))):
		b.append(z[x])
		if len(b) == 1:
			continue
		c = b[-2]+b[-1]
		if c in combtrans.keys():
			b = b[:-2]
			b.append(combtrans[c])
		for asdf in ertrans:
			if asdf[0] in b and asdf[1] in b:
				b = []
		else:
			pass
	
			
	print("Case #"+str(i+1)+": "+repr(b).replace("'", ""), file=open(out, 'a'))

	

