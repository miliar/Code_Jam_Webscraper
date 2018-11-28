text = open("A-small-attempt0.in.txt", "r")
i = int(text.readline())
for j in range(1,i+1):
	line1 = int(text.readline())
	for k in range(0, 4):
		if k == line1-1:
			L1 = map(int, text.readline().split(' '))
		else:
			text.readline()
	line2 = int(text.readline())
	for k in range(0, 4):
		if k == line2-1:
			L2 = map(int, text.readline().split(' '))
		else:
			text.readline()
	found = []
	for k in range(0,4):
		for l in range(0,4):
			if L1[k] == L2[l]:
				found = found+[L1[k]]
	if len(found) == 1:
		print('Case #'+str(j)+': '+str(found[0]))
	elif len(found) > 1:
		print('Case #'+str(j)+': '+'Bad magician!')
	else:
		print('Case #'+str(j)+': '+'Volunteer cheated!')