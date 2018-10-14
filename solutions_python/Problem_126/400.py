
f = open("in.txt")
o = open("output.txt", "w+")

for case in range(int(f.readline())):
	parts = f.readline().split()
	name = parts[0]
	n = int(parts[1])
	tot = 0

	for i in range(n, len(name)+1):
		for j in range(len(name)+1-i):
			conCount = 0
			for k in range(j, j+i):
				if (name[k] not in ['a', 'e', 'i', 'o', 'u']):
					conCount += 1
					if conCount == n:
						tot += 1
						break
				else:
					conCount = 0

	o.write("Case #" + str(case+1) + ": "+ str(tot) + "\n")
o.close()