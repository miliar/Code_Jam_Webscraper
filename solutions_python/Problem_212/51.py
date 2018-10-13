import math

fi = open("A-large.in","r")
fo = open("output","w")
numinst = int(fi.readline())
for k in range(numinst):
	inst1 = fi.readline().split()
	p = int(inst1[1])
	inst2 = fi.readline().split()
	groups = [0 for _ in range(p)]
	for c in inst2:
		groups[int(c)%p] += 1
	happy_groups = 0
	happy_groups += groups[0]
	if (p==2):
		happy_groups += int(math.ceil((groups[1])/2.0))
	if (p==3):
		alt = min(groups[1],groups[2])
		happy_groups += alt
		happy_groups += int(math.ceil((groups[1]+groups[2]-2*alt)/3.0))
	if (p==4):
		firstmod2 = groups[2]/2
		happy_groups += firstmod2
		remainingmod2 = groups[2]-2*firstmod2
		alt = min(groups[1],groups[3])
		happy_groups += alt
		happy_groups += int(math.ceil((groups[1]+groups[3]-2*alt+2*remainingmod2)/4.0))
	fo.write("Case #"+str(k+1)+": "+str(happy_groups)+"\n")
	print k
fo.close()
fi.close()