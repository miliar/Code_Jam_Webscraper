def gcd(num1,num2):
	if num1==0:
		return num2
	elif num2==0:
		return num1
	elif num1==1 or num2==1:
		return 1
	else:
		if num1>num2:
			factor=num1/num2
			return gcd(num1-factor*num2,num2)
		else:
			factor=num2/num1
			return gcd(num1, num2-factor*num1)


f=open('C:/Users/Meir/python/codejam/Cinput2.txt', 'r')
g=open('C:/Users/Meir/python/codejam/Coutput2.txt', 'w')	
TestSize=0

aline=f.readline()
bline=aline.split(" ")

Testsize=int(bline[0])

for idx in range(Testsize):
	aline=f.readline()
	bline=aline.split(" ")
	numbers=int(bline[0])
	thenums=[]
	for idx2 in range(1,numbers):
		thenums.append(int(bline[idx2]))
	thenums.append(int(bline[numbers][:-1]))
	thenums.sort()
	#print thenums
	newnums=[]
	for idx3 in range(1,numbers):
		newnums.append(int(thenums[idx3])-int(thenums[0]))
	#print newnums
	gcdcur=newnums[0]
	for idx4 in range(1,numbers-1):
		gcdcur=gcd(gcdcur,newnums[idx4])
	gcdfinal=gcdcur
	#print gcdfinal
	mod=thenums[0]%gcdfinal
	if mod==0:
		difference=0
	else:
		difference=gcdfinal-mod
	g.write("Case #" + str(idx+1)+": " + str(difference)+"\n")

	 
