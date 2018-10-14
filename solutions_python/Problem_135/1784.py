
def solver(row1, row2, lists1, lists2):
	first = set(lists1[row1])
	second = set(lists2[row2])
	print first 
	print second
	union = first & second
	if len(union) >1:
		return "Bad magician!"
	elif len(union) <1:
		return "Volunteer cheated!"
	else:
		return list(union)[0]

with open("A-small-attempt0.in") as inp:
	inp = inp.read()
	with open("output", "w") as out:
		inp = inp.split("\n")
		n = int(inp.pop(0))
		for i in xrange(n):
			row1 = int(inp.pop(0))-1
			lists1 = [inp.pop(0).split() for j in xrange(4)]
			row2 = int(inp.pop(0))-1
			lists2 = [inp.pop(0).split() for j in xrange(4)]
			o = solver(row1, row2, lists1, lists2)
			out.write("Case #%d: %s\n"%(i+1, o))
