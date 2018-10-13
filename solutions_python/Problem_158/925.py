f = open('D-small-attempt2.in', 'r')
ans = open('result.txt', 'w')

T = int(f.readline().strip())

for t in xrange(0, T):
	line = f.readline().strip()

	parts = [int(x.strip()) for x in line.split(" ")]

	X = parts[0]
	R = parts[1]
	C = parts[2]

	if X == 1:
		ans.write("Case #"+str(t+1)+": GABRIEL" + '\n')
	elif X == 2:
		if (R * C) % 2 == 0:
			ans.write("Case #"+str(t+1)+": GABRIEL" + '\n')
		else:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n')
	elif X == 3:
		if R < 3 and C < 3:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		elif R == 3 and C in [1]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		elif R in [1] and C in [1,2,3,4]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		elif R in [2] and C in [1,2,4]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		elif R == 4 and C in [1, 2, 4]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		else:
			ans.write("Case #"+str(t+1)+": GABRIEL" + '\n') 
	elif X == 4:
		if R < 4 and C < 4:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n')
		elif R == 4 and C in [1, 2]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		elif R in [1,2] and C in [1, 2, 3, 4]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n')
		elif R in [3] and C in [1, 2, 3]:
			ans.write("Case #"+str(t+1)+": RICHARD" + '\n') 
		else:
			ans.write("Case #"+str(t+1)+": GABRIEL" + '\n') 
	#ans.write("Case #"+str(t+1)+": " +str(invited)+ '\n')