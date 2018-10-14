
fin = open("A-small-attempt0.in", "r")
fout = open("out", "w")
T = int(fin.readline())
for i in range(T):
	c1 = int(fin.readline())
	arr1 = set([[int(g) for g in fin.readline().split()] for x in range(4)][c1-1])
	c2 = int(fin.readline())
	arr2 = set([[int(g) for g in fin.readline().split()] for x in range(4)][c2-1])
	intersection = arr1 & arr2
	intersectionCount = len(intersection)
	if intersectionCount == 1:
		ans = str(list(intersection)[0])
	elif intersectionCount == 0:
		ans = "Volunteer cheated!"
	else:
		ans = "Bad magician!"
	fout.write("Case #" + str(i+1) + ": " + ans + '\n')
fout.close()