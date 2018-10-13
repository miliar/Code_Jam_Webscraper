def equal(n):
	for i in range(len(n)-1):
		if n[i] != n[i+1]:
			return False
	return True		

f = open("C-small-attempt2.in")
g = open("resultado3.txt", 'w')
f.readline()
index = 1
for line in f:
	parejas = {}
	line = line.strip()
	line = line.split()
	inf = int(line[0])
	sup = int(line[1])
	aux = 0	
	for i in range(inf, sup+1):
		tmp = str(i)
		for j in range(len(tmp)-1):
			tmp = tmp[-1] + tmp[:-1]
			if sup >= int(tmp) and int(tmp) >= inf and len(str(i)) == len(str(int(tmp))) and not((len(tmp) % 2 == 0) and (tmp[:len(tmp)/2] == tmp[(len(tmp)/2):]) and equal(tmp[:len(tmp)/2]) and equal(tmp[(len(tmp)/2):])):
				if (i, int(tmp)) not in parejas and i < int(tmp):
					aux += 1
					parejas[(i, int(tmp))] = 1
					parejas[(int(tmp),i)] = 1

	g.write("Case #%s: %s \n" % (index, aux))
	index += 1