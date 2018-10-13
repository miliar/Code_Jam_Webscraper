f = open("input", 'r')
g = open("results", 'w')

active = ""
list1 = []
list2 = []

T = int(f.readline())
for i in range(1, T+1):
	active += "Case #" + str(i) + ": "
	row1 = int(f.readline())
	for j in range(1,5):
		if (j == row1):
			list1 = (f.readline()).split()
			print list1
		else:
			f.readline()
	row2 = int(f.readline())
	for j in range(1,5):
		if (j == row2):
			list2 = (f.readline()).split()
		else:
			f.readline()


	common = list(set(list1).intersection(set(list2)))
	print list1
	print list2
	if (len(common) >= 2):
		active += "Bad magician!\n"
	elif(len(common) == 0):
		active += "Volunteer cheated!\n"
	else:
		active += str(common[0]) + "\n"
	g.write(active)
	active = ""


