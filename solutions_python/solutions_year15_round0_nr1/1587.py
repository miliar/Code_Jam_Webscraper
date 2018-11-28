import re

f = open("A-large.in","r")
w = open("output_aLarge.txt","w")
num = f.readline()
for i in range(0,int(num)):
	res = 0
	smax,aud = [str(l) for l in f.readline().split()]
	clap = int(aud[0])
	for j,nSi in enumerate([int(x) for x in aud]):
		if j == 0:
			continue
		else:
			if nSi > 0:
				if clap < j:
					invite = j-clap
					res+=invite
					clap+=nSi+invite
				else:
					clap+=nSi
	print("Case #{0}: {1} ".format(i+1,res))
	w.write("Case #{0}: {1}\n".format(i+1,res))
w.close()