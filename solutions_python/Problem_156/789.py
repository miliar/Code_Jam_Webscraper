tests = int(raw_input())
for t in range(tests):
	nonempty = int(raw_input())
	pancakes = [int(k) for k in raw_input().split(" ")]

	ferdig = False
	maksimal = max(pancakes)
	beste = max(pancakes)
	split = 0
	while not ferdig:
		maksimal = max(pancakes)
		for s in range(len(pancakes)):
			if pancakes[s] == maksimal:
				del pancakes[s]
				break
		if maksimal == 9 and 5 not in pancakes and 9 not in pancakes:
			pancakes.append(6)
			pancakes.append(3)
		else:
			pancakes.append(maksimal/2)
			pancakes.append(maksimal-(maksimal/2))
		split += 1
		storste = max(pancakes)
		if storste + split < beste:
			beste = storste + split
		if storste == 1:
			ferdig = True
	print 'Case #{}: {}'.format(t+1,beste)