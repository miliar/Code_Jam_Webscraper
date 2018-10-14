def ListComparer(A,B):
	C = sorted(A + B)
	D = []
	for i in range(1,len(C)):
		if C[i] == C[i-1]:
			D.append(C[i])
	return(D)



def InputTaker(Filename):
	Input = open(Filename,"r")
	return(Input)

f = InputTaker("A-small-attempt0.in.txt")
file = open("MagicOutput.txt", "w")

a = int(f.readline())

for i in range(0,a):
	b = int(f.readline())
	for j in range(0,4):
		cline = f.readline()
		if j == b-1:
			A = map(int, cline.split())
	c = int(f.readline())
	for k in range(0,4):
		cline = f.readline()
		if k == c-1:
			B = map(int, cline.split())
	d = ListComparer(A,B)
	if len(d)==0:
		file.write("Case #"+str(i+1)+": Volunteer cheated! \n")
	elif len(d)==1:
		file.write("Case #"+str(i+1)+": "+str(d[0])+"\n")
	else:
		file.write("Case #"+str(i+1)+": Bad magician! \n")