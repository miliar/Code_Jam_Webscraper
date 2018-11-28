fp.close()
fp=open('A-small-attempt0.in','r')
ll=fp.readline()
fout=open('out.txt','w')
for i in range(int(ll)):
	a=4*["1"]
	b=[[0]*4 for u in range(4)]
	flag=0
	for j in range(4):
		a[j]=fp.readline()[0:-1]
	for k in range(4):
		for l in range(4):
			if(a[k][l]=='X'):
				b[k][l]=5
			elif(a[k][l]=='O'):
				b[k][l]=32
			elif(a[k][l]=='.'):
				b[k][l]=-1
	for k in range(4):
		suma=0
		for l in range(4):
			suma+=b[k][l]
		if(suma==15 or suma==20):
			flag=1
		elif(suma==96 or suma==128):
			flag=2
	if(flag==0):
		for k in range(4):
			suma=0
			for l in range(4):
				suma+=b[l][k]
			if(suma==15 or suma==20):
				flag=1
			elif(suma==96 or suma==128):
				flag=2
	if(flag==0):
		suma=0
		for k in range(4):
			suma+=b[k][k]
			if(suma==15 or suma==20):
				flag=1
			elif(suma==96 or suma==128):
				flag=2
	if(flag==0):
		suma=0
		for k in range(4):
			suma+=b[3-k][k]
			if(suma==15 or suma==20):
				flag=1
			elif(suma==96 or suma==128):
				flag=2
	if(flag==0):
		for k in range(4):
			for l in range(4):
				if(b[k][l]==-1):
					flag=3
	if(flag==0):
		fout.write("Case #%d: Draw\n"%(i+1))		
	elif(flag==1):
		fout.write("Case #%d: X won\n"%(i+1))	
	elif(flag==2):
		fout.write("Case #%d: O won\n"%(i+1))
	elif(flag==3):
		fout.write("Case #%d: Game has not completed\n"%(i+1))
	fp.readline()
	if(i==1):
		print b
	print a


fp.close()
fout.close()


