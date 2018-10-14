file = open("2014Asample.txt")
out = open("2014A.out", "w")

for i in range(int(file.readline())):
	row1 = int(file.readline()) - 1
	grid1 = [set(map(int, file.readline().split(" "))) for x in range(4)]
	row2 = int(file.readline()) - 1
	grid2 = [set(map(int, file.readline().split(" "))) for x in range(4)]
	intersect = grid1[row1] & grid2[row2]
	if len(intersect) == 1:
		out.write("Case #" + str(i+1) + ": " + str(intersect.pop()) + "\n")
	elif len(intersect) == 0:
		out.write("Case #%s: Volunteer cheated!\n" % (i+1))
	else:
		out.write("Case #%d: Bad magician!\n" % (i+1))

out.close()