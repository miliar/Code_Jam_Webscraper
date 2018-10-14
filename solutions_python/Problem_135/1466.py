Output = []
T = int(raw_input())
for i in range(T):
	row = int(raw_input())
	for j in range(4):
		line = raw_input()
		if row==j+1:
			Set1 = line.split()
	row = int(raw_input())
	for j in range(4):
		line = raw_input()
		if row==j+1:
			Set2 = line.split()
	outval = 0
	outcount = 0
	for val in Set1:
		if val in Set2:
			outval = val
			outcount += 1
	if outcount==0:
		Output += ["Volunteer cheated!"]
	elif outcount==1:
		Output += [outval]
	else:
		Output += ["Bad magician!"]
		
for i in range(len(Output)):
	print 'Case #%d: %s' % (i+1, Output[i])