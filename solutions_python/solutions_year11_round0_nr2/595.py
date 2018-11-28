inp = file("inp").read().split("\n")
for x, t in enumerate(inp[1:-1]):
	t = t.split(" ")
	combs = {}
	for zx in t[1:int(t[0]) + 1]:
		combs[zx[:2]] = zx[2]
		combs[zx[1] + zx[0]] = zx[2]
	t =  t[int(t[0]) + 1:]
	oppos = {}
	for zx in t[1:int(t[0]) + 1]:
		oppos[zx[0]] = oppos.get(zx[0], [])
		oppos[zx[0]].append(zx[1])
		oppos[zx[1]] = oppos.get(zx[1], [])
		oppos[zx[1]].append(zx[0])
	t =  t[int(t[0]) + 2:][0]
	magick = []
	i = -1
	while i < len(t) - 1:
		i += 1
		magick.append(t[i])
		if len(magick) > 1:
			tail = "".join(magick[-2:])
			if tail in combs:
				magick[-2:] = combs[tail]
				continue
		if t[i] in oppos:
			for gf in oppos[t[i]]:
				if gf in magick:
					magick = []
					break
	print "Case #" + str(x + 1) + ": [" + ", ".join(magick) + "]"
	
