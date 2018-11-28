import math

inp = open("Input.txt").readlines()
out = open("Output.txt",'w')

for j in range(int(inp[0].strip())):
	i = j+1
	tmp = inp[i].strip().split()
	C = float(tmp[0])
	F = float(tmp[1])
	X = float(tmp[2])
	farms = math.ceil(((F*X-2*C)/(F*C))-1)
	if farms<=0:
		time = X/2
	else:
		time = 0.0
		for n in range(int(farms)):
			time += C/(2+n*F)
		time += X/(2+farms*F)
	out.write("Case #"+str(i)+": "+str(time)+"\n")

out.close()