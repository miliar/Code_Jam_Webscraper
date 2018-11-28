f = file("A-large.in", "r")
of = file("A-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
line = 1
for case in range(cases):
	input = lines[line].split(" ");
	n = int(input[0])
	m = int(input[1])
	line += 1

	count = 0	
	root = {}

	print "exists"		
	for i in range(n):
		path = lines[line].strip()[1:].split("/");
		print path
		
		curr = root
		for p in path:
			if not curr.has_key(p):
				curr[p] = {}
				
			curr = curr[p]
		
		line += 1

	print "new"
	for i in range(m):
		path = lines[line].strip()[1:].split("/");
		
		curr = root
		for p in path:
			if not curr.has_key(p):
				curr[p] = {}
				count += 1
				
			curr = curr[p]
		
		line += 1
		
	of.write("Case #%d: %d\n" % (case + 1, count))
