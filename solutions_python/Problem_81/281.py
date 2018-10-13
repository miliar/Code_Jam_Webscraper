filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

res = []

n=1
while n!=len(ipt):
	teams = int(ipt[n])
	
	wp = []
	wp2 = []
	opps = []
	for i in range(n+1,n+1+teams):
		w=0
		l=0
		op=[]
		for q in range(len(ipt[i])):
			if ipt[i][q]=="1":
				w+=1
			if ipt[i][q]=="0":
				l+=1
			if ipt[i][q]==".":
				op.append(0)
			elif ipt[i][q] == "1" or ipt[i][q] == "0":
				op.append(1)
		wp.append(w/(w+l))
		wp2.append([w,w+l])
		opps.append(op)
	print(n,opps)
	
	owp = []
	for i in range(len(wp)):
		t=0
		p=0
		for q in range(len(wp)):
			print(n,i,q)
			if i==q:
				continue
			if opps[i][q] == 1:
				v=0
				if ipt[n+i+1][q] == "0":
					v=-1
				s = wp2[q][0] + v
				z = wp2[q][1] - 1
				print(n,i,wp2[q][0],s,z)
				r=s/z
				print(r)
				t+=r
				p+=1
		owp.append(t/p)
		
	oowp = []
	for i in range(len(owp)):
		t=0
		p=0
		for q in range(len(owp)):
			if i==q:
				continue
			else:
				if opps[i][q] == 1:
					t+=owp[q]
					p+=1
		oowp.append(t/p)
	
	rpi = []
	for i in range(len(wp)):
		rpi.append(.25*wp[i] + .5*owp[i] + .25*oowp[i])
	
	res.append(rpi)
	n=n+1+teams
	
tostr = ""
for n in range(len(res)):
	tostr+="Case #" + str(n+1) + ":\n"
	for i in res[n]:
		tostr+=str(i) + "\n"
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])
s=input("Die Zeit ist um.")