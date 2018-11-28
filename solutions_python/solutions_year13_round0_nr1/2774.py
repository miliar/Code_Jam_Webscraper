input_file = open('A-small-attempt8.in')
output_file = open('output.txt','r+')

for case in range(int(input_file.readline())):
	line=[]
	x=0
	y=[]
	z=[]
	ans=""
	option =0
	for i in range(4):
		line.append(input_file.readline().strip())

	e = input_file.readline()
	while x<4:
		if "XXX" in line[x] and "T" in line[x]:
			ans= "X won"
			x=4
		elif "OOO" in line[x] and "T" in line[x]:
			ans= "O won"
			x=4
		elif "XXXX" in line[x]:
			ans = "X won"
			x=4
		elif "OOOO" in line[x]:
			ans = "O won"
			x=4
		x+=1	
	if ans=="" and option==0:
		b=0
		flipx=0
		while b<4:
			a=0
			tempflip=""
			while a<4:
				tempflip+=line[a][b]
				a+=1
			b+=1
			tempflip = "".join(sorted(tempflip))
			y.append(tempflip)
		while flipx<4:
			if "XXX" in y[flipx] and "T" in y[flipx]:
				ans= "X won"
				flipx=4
			elif "OOO" in y[flipx] and "T" in y[flipx]:
				ans= "O won"
				flipx=4
			elif "XXXX" in y[flipx]:
				ans = "X won"
				flipx=4
			elif "OOOO" in y[flipx]:
				ans = "O won"
				flipx =4
			flipx+=1
		option =2
		if ans=="" and option==2:
			b=0
			a=3
			ab=0
			flipx=0
			tempflip1=""
			tempflip2=""
			while b<4:
				tempflip1+=line[b][b]
				b+=1
			z.append(tempflip1)
			while a>=0:
				tempflip2+=line[ab][a]
				a-=1
				ab+=1
			z.append(tempflip2)
			while flipx<2:
				if "XXX" in z[flipx] and "T" in z[flipx]:
					ans= "X won"
					flipx=4
				elif "OOO" in z[flipx] and "T" in z[flipx]:
					ans= "O won"
					flipx=4
				elif "XXXX" in z[flipx]:
					ans = "X won"
					flipx=4
				elif "OOOO" in z[flipx]:
					ans = "O won"
					flipx =4
				flipx+=1
	if ans=="" and "...." in line :
		ans = "Game has not completed"
	elif ans=="" and  "...." not in line:
		ans = "Draw"
	
	output_file.write("Case #{0}: {1}\n".format(case+1,ans))
input_file.close()
output_file.close()				

