fin = open("C-small-attempt0.in.txt")
fout = open("outputB.out",'w')
num = int(fin.readline())
counter = 0
casenum = 1

def c(n,x,y):
	m = []
	for i in range(1,len(str(n))):
		count = [n]
		rev = int(''.join(i for i in [str(n)[i:],str(n)[:i]]))
		if x <= rev <= y and rev != n: count.append(rev)
		if sorted(count) not in m: m.append(sorted(count))
	return m


while casenum <= num:
	count = []
	line = fin.readline()
	x = int(line[:line.index(" ")])
	y = int(line[line.index(" "):])
	for a in range(x,y+1):
		for i in c(a,x,y):
			if len(i) == 2 and i not in count: count.append(i)
	caser = "Case #" + str(casenum) + ": " + str(len(count)) + '\n'
	fout.write(caser)
	casenum += 1

fin.close()
fout.close()