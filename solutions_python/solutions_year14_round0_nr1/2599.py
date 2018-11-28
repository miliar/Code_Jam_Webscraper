import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for caseno in range(t):
	arr1 = []
	arr2 = []
	ans1 = int(f.readline()) - 1
	for i in range(4):
		ip = f.readline()
		arr1.append([int(x) for x in ip.split()])
	ans2 = int(f.readline()) - 1
	for i in range(4):
		ip = f.readline()
		arr2.append([int(x) for x in ip.split()])
	matches = set(arr1[ans1]) & set(arr2[ans2])
	print "Case #"+str(caseno+1)+":",
	if len(matches) == 0:
		print "Volunteer cheated!"
	elif len(matches) > 1:
		print "Bad magician!"
	elif len(matches) == 1:
		card = matches.pop()
		print card
