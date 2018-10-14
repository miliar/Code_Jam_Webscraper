input=open("a.in")


N=int(input.readline())
for caso in range(N):
	i=int(input.readline())
	leidos=1
	while i>1:
		input.readline()
		i-=1
		leidos+=1
	posibles=map(int,input.readline().split(" "))
	while leidos<4:
		input.readline()
		leidos+=1
	
	i=int(input.readline())
	leidos=1
	while i>1:
		input.readline()
		i-=1
		leidos+=1
	otros=map(int,input.readline().split(" "))
	reales=[]
	print "Case #"+str(caso+1)+':',
	for pos in posibles:
		if pos in otros:
			reales.append(pos)
	if len(reales)==1:
		print reales[0]
	elif len(reales)>1:
		print "Bad magician!"
	else:
		print "Volunteer cheated!"
	while leidos<4:
		input.readline()
		leidos+=1
