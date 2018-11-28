t = int(input())

for k in range(t):
	inp = input().split()
	smax = int(inp[0])
	ppl = [int(inp[1][i]) for i in range(smax+1)]

	parados = 0
	invitados = 0

	for sl in range(smax+1):
		if sl <= parados:
			parados += ppl[sl]
		else:
			if ppl[sl] > 0:
				invitados += sl-parados
				parados += invitados+ppl[sl]

	print ("Case #{}: {}".format(k+1,invitados))