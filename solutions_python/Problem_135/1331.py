def intersect(l1, l2):
	
	rez = 0
	for i in range(0,4):
		for j in range(0,4):
			if l1[i] == l2[j]:
				if rez != 0:
					return -1
				else:
					rez = l1[i]
	
	return rez

l1 = []
l2 = []

n = int(raw_input())
for j in range(1,n+1):
	inda = int(raw_input())
	for i in range(1,5):
		line = raw_input()
		if i == inda:
			l1 = line.split()

	indb = int(raw_input())
	for i in range(1,5):
		line = raw_input()
		if i == indb:
			l2 = line.split()
	
	#print l1
	#print l2
	str = ""
	str = "Case #%d: " % j
	r = intersect(l1, l2)
	if r == 0:
		str += "Volunteer cheated!"
	else:
		if r == -1:
			str += "Bad magician!"
		else:
			str += (r)
	
	print str
			