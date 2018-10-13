file = open("R.txt", "r").read(100000)

filename = "out.txt"

out = open(filename, 'w')

parts = file.split("\n")
n = int(parts.pop(0))

for i in range(1,n+1):
	line = parts.pop(0)
	fields = line.split(" ")
	order = []
	fields.pop(0)
	while len(fields) > 0:
		a = fields.pop(0)
		b = fields.pop(0)
		order.append((a, int(b)))
	O = 1
	B = 1
	usedO = 0
	usedB = 0
	total = 0
	
	while len(order) > 0:
		mv = order.pop(0)
		if mv[0] == "O":
			usedO = (abs(O - mv[1]) - min(abs(O - mv[1]), usedB)) + 1
			O = mv[1]
			while len(order) > 0 and order[0][0] == mv[0]:
				mv = order.pop(0)
				usedO += abs(O - mv[1]) + 1
				O = mv[1]
			total += usedO
		else:
			usedB = (abs(B - mv[1]) - min(abs(B - mv[1]), usedO)) + 1
			B = mv[1]
			while len(order) > 0 and order[0][0] == mv[0]:
				mv = order.pop(0)
				usedB += abs(B - mv[1]) + 1
				B = mv[1]
			total += usedB
	
	
	out.write(("Case #%d: %d\n" % (i, total)))
	"""
	while len(order) > 0:
		mv = order.pop(0)
		
		if mv[0] == "O":
			if last[0] == "O":
				usedB = 0
			used = abs(O - mv[1]) - min(usedB, abs(O - mv[1]))
			total += used + 1
			usedO += used + 1
			O = mv[1]
		else:
			if last[0] == "B":
				usedO = 0
			used = abs(B - mv[1]) - min(usedO, abs(B - mv[1]))
			total += used + 1
			usedB += used + 1
			B = mv[1]
		last = mv
	out.write(("Case #%d: %d\n" % (i, total)))
	"""