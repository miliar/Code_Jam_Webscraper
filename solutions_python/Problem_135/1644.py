fileHandle = open("in.txt", "r")
fileHandle2 = open("out.txt", "w")
T = int(fileHandle.readline())
for c in range(T):
	fileHandle2.write("Case #" + str(c+1) + ": ")
	ans1 = int(fileHandle.readline())
	for i in range(4):
		line = fileHandle.readline()
		if i == ans1 - 1:
			l = line.split(" ")
			l1 = [int(x) for x in l]
	ans2 = int(fileHandle.readline())
	for i in range(4):
		line = fileHandle.readline()
		if i == ans2 - 1:
			l = line.split(" ")
			l2 = [int(x) for x in l]
	result = set(l1) & set(l2)
	if len(result) == 0:
		fileHandle2.write("Volunteer cheated!")
	elif len(result) == 1:
		fileHandle2.write(str((list(result))[0]))
	else:
		fileHandle2.write("Bad magician!")
	fileHandle2.write("\n")
fileHandle.close()
fileHandle2.close()
