
def move_O():
	global O,I,o, flag
	if len(O) > 0:
		if O[0] > o: o += 1
		elif O[0] < o: o -= 1
		elif I[0] == 'O':
			del O[0]
			del I[0]
			flag = True
			
def move_B():
	global B,I,b, flag
	if len(B) > 0:
		if B[0] > b: b += 1
		elif B[0] < b: b -= 1
		elif I[0] == 'B' and not flag:
			del B[0]
			del I[0]

f = open("input.txt", "r")
w = open("output.txt", "w")
cases = int(f.readline())
o, b = 1, 1
O, B, I = [], [], []
flag = False
for case in range(1, cases+1):	
	o, b = 1, 1
	O, B, I = [], [], []
	line = f.readline().strip()
	parts = line.split(' ')
	count = int(parts[0])
	del parts[0]
	if count == 0:
		print "Case #%d: %d" % (case, 0)
		continue
	
	while len(parts) > 0:
		I.append(parts[0])
		val = int(parts[1])
		if parts[0] == 'O': O.append(val)		
		else: B.append(val)
		del parts[0] #remove label
		del parts[0] #remove value
	
	t = 0
	while len(I) > 0:
		flag = False
		move_O()
		move_B()
		t += 1
	w.write("Case #%d: %d\n" % (case, t))
	#print "Case #%d: %d" % (case, t)
f.close()	
w.close()
	