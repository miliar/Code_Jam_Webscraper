data = open("D-small-attempt1.in","r")
outfile = open("cj_ominoes_small.txt","w")

t = int(data.readline())
for case in range(0,t):
	xrc = data.readline().split(' ')
	if case!=t-1:
		xrc[-1]=xrc[-1][:-1]
	for i in range(0,len(xrc)):
		xrc[i]=int(xrc[i])
	print xrc
	
	x = xrc[0]
	r = xrc[1]
	c = xrc[2]
	
	outfile.write("Case #" + str(case+1) + ": ")
	
	if x >= 7: outfile.write("RICHARD")
	elif (r*c)%x!=0: outfile.write("RICHARD")
	elif x==1:
		outfile.write("GABRIEL")
	elif x==2:
		if (r<=1) & (c<=1): outfile.write("RICHARD")
		else: outfile.write("GABRIEL")
	elif x==3:
		if (r<=1) | (c<=1): outfile.write("RICHARD")
		else: outfile.write("GABRIEL")
	elif x==4:
		if (r==2) & (c==4): outfile.write("RICHARD")
		elif (r==4) & (c==2): outfile.write("RICHARD")
		elif (r<=1) | (c<=1): outfile.write("RICHARD")
		elif (r in [2,3]) & (c in [2,3]): outfile.write("RICHARD")
		else: outfile.write("GABRIEL")
	elif x==5:
		if (r<=2) | (c<=2): outfile.write("RICHARD")
		elif (r in [3,4]) & (c in [3,4]): outfile.write("RICHARD")
		else: outfile.write("GABRIEL")
	elif x==6:
		if (r<=2) | (c<=2): outfile.write("RICHARD")
		elif (r in [3,4,5]) & (c in [3,4,5]): outfile.write("RICHARD")
		else: outfile.write("GABRIEL")
		
	if case!=t-1:
		outfile.write("\n")