filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

for n in range(len(ipt)):
	ipt[n] = ipt[n][:-1]

res = []

n=1
while n<len(ipt):
	a = ipt[n].split()
	for i in range(len(a)):
		a[i] = int(a[i])
	
	tilear=[]	
	for i in range(n+1, n+1+a[0]):
		s=[]
		for q in ipt[i]:
			if q==".":
				s.append(0)
			elif q=="#":
				s.append(1)
		tilear.append(s)
	print(n,a[0],tilear)
	if (a[0] == 1 and a[1] == 2) or (a[0] == 2 and a[1] == 1):
		s=''
		for i in tilear:
			for j in i:
				s+=j
		r=0
		for i in s:
			if i=="1":
				r=1
		if r==1:
			res.append("\nImpossible")
			n=n+a[0]+1
			continue
		else:
			bb=''
			for i in tilear:
				aa=''
				for j in i:
					aa+=j
				bb+=aa+"\n"
			for i in range(len(bb)):
				if bb[i]==0:
					bb = bb[0:i]+"."+bb[i+1:]
				elif bb[i]==2:
					bb = bb[0:i]+"#"+bb[i+1:]
			bb="\n"+bb[:-1]
			res.append(bb)
			n=n+a[0]+1
			continue
	
	for i in range(0,len(tilear)-1):
		for j in range(0,len(tilear[i])-1):
			print(tilear[i][j],tilear[i][j+1],tilear[i+1][j],tilear[i+1][j+1])
			if tilear[i][j] == 1 and tilear[i][j+1] == 1 and tilear[i+1][j] == 1 and tilear[i+1][j+1] == 1:
				print('hi')
				tilear[i][j] = "/"
				tilear[i][j+1] = "\\"
				tilear[i+1][j] = "\\"
				tilear[i+1][j+1] = "/"
	print(tilear)
	s=''
	for i in tilear:
		for j in i:
			s+=str(j)
	r=0
	for i in s:
		if i=="1":
			r=1
	if r==1:
		res.append("\nImpossible")
		n=n+a[0]+1
		continue
	else:
		bb=''
		for i in tilear:
			aa=''
			for j in i:
				if j==0:
					j="."
				aa+=str(j)
			bb+=aa+"\n"
		bb="\n"+bb[:-1]
		res.append(bb)
		n=n+a[0]+1
		continue
	
tostr = ""
for n in range(len(res)):
	tostr+="Case #" + str(n+1) + ":" + str(res[n]) + "\n"
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])
s=input("Die Zeit ist um.")