#!/usr/bin/python
fin = open("A-large.in.txt")
fout = open("A-large.out.txt",'w')
T = int(fin.readline())
for i in range(T):
	fout.write("Case #%d: "%(i+1))
	n, data = fin.readline().split(' ')
	n = int(n)
	need = 0
	tot = t = int(data[0])
	for j in range(1,n+1):
		t = int(data[j])
		tmp = j - tot
		if tmp > 0:
			if need < j-tot:
				need = j-tot
		tot = tot + t
	fout.write(str(need))
	fout.write("\n")
fout.close()
fin.close()