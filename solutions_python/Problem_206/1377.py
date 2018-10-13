
def readNSolve():
	f=open("A-large.in")
	out=open("A-large.out","a")
	T=int(f.readline())
	lines=f.readlines()
	j = 0
	for i in range(T):
		splits=lines[i+j].split(" ")
		distance,numHorse=int(splits[0]),int(splits[1])
		maxSlow=0
		for k in range(1,numHorse+1):
			otherHorseSplit=lines[i + j + k].split(" ")
			start,speed=int(otherHorseSplit[0]),int(otherHorseSplit[1])
			slow=(distance-start)*1.0/speed
			maxSlow=max(maxSlow,slow)
		j+=numHorse
		out.write("Case #{}: {}\n".format((i+1),round(distance*1.0/maxSlow,6)))
	out.close()
	f.close()
readNSolve()