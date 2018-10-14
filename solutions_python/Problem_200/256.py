inp = open("b.in", "r")
T = int(inp.readline())
oup = open("b.out", "w")
for t in range(T):
	x = int(inp.readline())
	x+=1
	x*=9
	x = str(x)
	y = 9
	for i in range(len(x)):
		if (y >= int(x[i])):
			y-= int(x[i])
		else:
			x = x[0:i] + str(y) + x[i+1:]
			y=0
	x = int(x)
	x//=9
	x-=1
	oup.write("Case #" + str(t+1) + ": " + str(x)+"\n")	