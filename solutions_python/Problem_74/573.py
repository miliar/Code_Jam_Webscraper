inp = file("inp").read().split("\n")
for x, t in enumerate(inp[1:-1]):
	oseq = []
	bseq = []
	pseq = []
	cur = None
	for n in t.split(" ")[1:]:
		if cur == None:
			cur = n
			continue
		n = int(n)
		if cur == "B":
			bseq.append(n)
		else:
			oseq.append(n)
		pseq.append(cur)
		cur = None
	moves = 0
	opos = 1
	bpos = 1
	while len(pseq) > 0:
		js = False
		if len(bseq) > 0:
			if bpos == bseq[0] and pseq[0] == "B":
				bseq.pop(0)
				pseq.pop(0)
				js = True
			elif bpos < bseq[0]:
				bpos += 1
			elif bpos > bseq[0]:
				bpos -= 1
		if len(oseq) > 0:
			if opos == oseq[0] and pseq[0] == "O" and not js:
				oseq.pop(0)
				pseq.pop(0)
			elif opos < oseq[0]:
				opos += 1
			elif opos > oseq[0]:
				opos -= 1
		moves += 1
	print "Case #" + str(x + 1) + ": " + str(moves)
