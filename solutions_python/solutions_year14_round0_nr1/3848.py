import re

lines = open("A-small-attempt1.in").readlines()


def intersection(list1, list2):
	l1 = list1.split(" ")
	l2 = list2.split(" ")
	j = 0
	possiblities = []
	for i in l1:
		if i in l2:
			j = j+1
			possiblities.append(i)
	if j == 1:
		return possiblities[0]
	if j == 0:
		return "Volunteer cheated!"
	return "Bad magician!"

i = 1
k = 1
while(i < len(lines)):
	row1num = lines[i].strip()
	row1 = lines[i + int(row1num)].strip()
	row2num = lines[i + 5].strip()
	row2 = lines[int(row2num) + i + 5].strip()
	i = i + 10
	#print row1, row2
	print "Case #%d:"%(k), intersection(row1, row2)
	k = k + 1