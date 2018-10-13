f = open('A-small-attempt0.in')
f2 = open('Output.txt','w')
T = f.readline().strip()
T = int(T)
for num in range(1,T+1):
	p1 = int(f.readline())
	for m in range(1,5):
		if m == p1:
			line1 = f.readline().strip().split(" ")
		else:
			f.readline()
	p2 = int(f.readline())
	for m in range(1,5):
		if m == p2:
			line2 = f.readline().strip().split(" ")
		else:
			f.readline()
	count = 0
	temp = 0
	for m in line1:
		for n in line2:
			if m == n:
				count += 1
				temp = m
	output="Case #" + str(num) + ": "
	if count == 1:
		output += temp
	if count == 0:
		output += "Volunteer cheated!"
	if count > 1:
		output += "Bad magician!"
	f2.write(output+"\n")
f2.close()
f.close()