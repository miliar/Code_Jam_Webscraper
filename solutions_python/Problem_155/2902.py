fi = open('in_a.txt', 'r'); fo = open('out_a.txt', 'w'); T = int(fi.readline());
for i in range(1,T+1):
	l = fi.readline().split()
	Smax = int(l[0])
	ppl = [int(l[1][j]) for j in range(Smax + 1)]
	inv,clapping = 0,0
	for shyness in range(Smax + 1):
		if clapping < shyness:
			inv += shyness - clapping
			clapping += (shyness - clapping)
		clapping += ppl[shyness]
	fo.write("Case #" + str(i) + ": " + str(inv) + "\n")
fo.close()
