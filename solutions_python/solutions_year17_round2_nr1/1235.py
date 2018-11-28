fi = open("A-large.in.txt","r")
fo = open("output","w")
numinst = int(fi.readline())
for k in range(numinst):
	inst = fi.readline().split()
	dest = int(inst[0])
	numhorses = int(inst[1])
	horses = []
	for k1 in range(numhorses):
		horse = fi.readline().split()
		horses += [(int(horse[0]),int(horse[1]))]
	horses.sort(key=lambda tup: tup[0], reverse=True)
	at_dest = [float(dest-horses[0][0])/horses[0][1]]
	for k1 in range(numhorses)[1:]:
		at_dest += [max(at_dest[k1-1],float(dest-horses[k1][0])/horses[k1][1])]
	fo.write("Case #"+str(k+1)+": "+str(dest/at_dest[numhorses-1])+"\n")
	print k
fo.close()
fi.close()
