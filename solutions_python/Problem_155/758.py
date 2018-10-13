f,out = open("input", "r"),open("output", "w")
T = int(f.readline())
for t in range(T):
	M,S = f.readline().split()
	s = [int(w) for w in S]
	x=s[0]
	y=0
	for i in range(1,int(M)+1):
		if i>x+y:
			y+=i-x-y
		x+=s[i]
	out.write("Case #" + str(t+1) +": " + str(y) + "\n")