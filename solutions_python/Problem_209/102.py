import math

fi = open("A-large.in.txt","r")
fo = open("output","w")
numinst = int(fi.readline())
for k in range(numinst):
	inst = fi.readline().split()
	available_cakes = int(inst[0])
	stacksize = int(inst[1])
	pancakes = []
	for j in range(available_cakes):
		pancake = fi.readline().split()
		pancakes += [(int(pancake[0]),int(pancake[1]))]
	sizes =[(2*math.pi*pancakes[i][0]*pancakes[i][1],math.pi*(pancakes[i][0]**2)) for i in range(available_cakes)] 
	sizes.sort(key=lambda tup: tup[0], reverse=True)
	print sizes
	surfaces = [sum([sizes[j][0] for j in (range(stacksize-1)+[i])])+max([sizes[j][1] for j in range(stacksize-1)+[i]]) for i in range(stacksize-1,available_cakes)]
	print surfaces
	fo.write("Case #"+str(k+1)+": "+str(max(surfaces))+"\n")
	print k
fo.close()
fi.close()