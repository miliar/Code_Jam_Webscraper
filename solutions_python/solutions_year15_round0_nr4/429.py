
f=open("D-small-attempt0.in","r")
g=open("OUTPUT.txt","w+")

T=int(f.readline())
for i in range(T):
	[X,R,C]=[int(j) for j in f.readline().split()]
	
	if X>=7 or ((R*C)%X)!=0:
		g.write("Case #{}: RICHARD\n".format(i+1));
	elif X==1 or X==2:
		g.write("Case #{}: GABRIEL\n".format(i+1));
	elif X==3:
		if R>=2 and C>=2:
			g.write("Case #{}: GABRIEL\n".format(i+1));
		else:
			g.write("Case #{}: RICHARD\n".format(i+1));
	elif X==4:
		if R<=2 or C<=2:
			g.write("Case #{}: RICHARD\n".format(i+1));
		else:
			g.write("Case #{}: GABRIEL\n".format(i+1));

f.close()
g.close()
