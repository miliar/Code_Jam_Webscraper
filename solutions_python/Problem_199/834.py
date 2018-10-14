f = open("A.in")
g = open("Aw.txt","w")
n = int(f.readline())
for i in range(n):
	line = f.readline().split()
	pancake = list(line[0])
	count = 0
	flag = 0
	for pi,p in enumerate(pancake):
		if p == "-" and pi <= len(pancake) - int(line[1]):
			for j in range(int(line[1])):
				if pancake[pi + j] == "-":
					pancake[pi + j] = "+"
				else:
					pancake[pi + j] = "-"
			count += 1
		elif p == "-" and pi > len(pancake) - int(line[1]):
			flag = 1
	if flag == 1:
		g.write(" ".join(["Case","#" + str(i + 1)+":","IMPOSSIBLE","\n"]))
	else:
		g.write(" ".join(["Case","#" + str(i + 1)+":",str(count),"\n"]))
	