f = open('A-small-attempt0.in','r')
T = int(f.readline().strip())
w = open('output.txt', 'w')
it = lambda x: int(x)
for z in range(T):
	r1 = int(f.readline().strip())-1
	arr = [x[:] for x in [[None]]*4]
	for i in range(4):
		arr[i] = map(it,f.readline().split())
	poss1 = arr[r1][:]#Deep copy
	r2 = int(f.readline().strip())-1
	for i in range(4):
		arr[i] = map(it,f.readline().split())
	poss2 = arr[r2][:]
	poss3 = []
	for i in range(4):
		for j in range(4):
			if poss1[i] == poss2[j]:
				poss3.append(poss1[i])
	print poss1
	print poss2
	w.write("Case #" + str(z+1) + ": ")
	if len(poss3) == 1:
		w.write(str(poss3[0])+"\n")
	elif len(poss3) == 0:
		w.write("Volunteer cheated!\n")
	else:
		w.write("Bad magician!\n")
f.close()
w.close()
