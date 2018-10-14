'''t = time(s)'''
k = 0
'''k for rate increment'''
r0 = 2.0
r = r0


f = open("B-large.in","r")
t = int(f.readline().strip())

w = open("Output.txt","w")

for t in range(1,t+1):
	l = f.readline()
	con = [float(s) for s in l.split()]
	C = con[0]
	F = con[1]
	X = con[2]

	ri = r
	Delta = C / ri
	r += F
	while (X / r + Delta) < (X / ri):
		'''buy'''
		k += 1
		r += F
		ri += F
		Delta = C / ri
	time = 0
	r = r0
	for k in range(0,k):
		time += C / r
		r += F
	time += X / r
	w.write("Case #"+str(t)+": "+str(time)+"\n")
	k = 0
	r = r0

w.close()
f.close
