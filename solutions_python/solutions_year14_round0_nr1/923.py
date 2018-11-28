T = int(raw_input())

for t in range(1, T+1):

	M1 = []
	ans1 = int(raw_input())
	for i in range(4):
		M1.append([int(x) for x in raw_input().split(' ')])

	M2 = []
	ans2 = int(raw_input())
	for i in range(4):
		M2.append([int(x) for x in raw_input().split(' ')])		
	
	a = []
	for x in M1[ans1 - 1]:
		if x in M2[ans2 - 1]:
			a.append(x)
			
	if len(a) == 1:
			answer = a[0]
	elif len(a) > 1:
		answer = "Bad magician!"
	else:
		answer = "Volunteer cheated!"

	print "Case #{0}: {1}".format(t, answer)
