c = open("data.in")
file = open("output.dat","w+")
y=c.readline()
case = 1
while y != [] :
	y= c.readline()
	j=y.split()
	o=0
	x=[]
	correct=[]
	#for making the testline
	for char in j[0]:
		x.append(char)
	step = 0
	i=0
	def flip(a):
		if a == '-':
			return '+'
		else:
			return '-'
	
	while i<=len(x)-int(j[1]):
		if(x[i] == '-'):
			dp =0
			while dp<int(j[1]):
				x[dp+i]=flip(x[dp+i])
				dp+=1
			step+=1
		i+=1

	while o<len(x):
		correct.append("+")
		o+=1
	if x==correct:
		print("Case #"+str(case)+":",step)
	else:
		print("Case #"+str(case)+": IMPOSSIBLE")
	case+=1