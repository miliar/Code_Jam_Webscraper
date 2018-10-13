filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

res = []
for n in range(1,ls+1):
	print(n)
	cln = ipt[n]
	cln = cln.split(" ")
	
	cmbn = 0
	excl = int(cln[cmbn]) + 1
	lvsr = int(cln[excl]) + excl + 1
	
	carr = []
	earr = []
	
	if int(cln[cmbn]) != 0:
		for n in range(cmbn+1,excl):
			carr.append([cln[n][0:2],cln[n][0:2][::-1],cln[n][2]])
			
	if int(cln[excl]) != 0:
		for n in range(excl+1,lvsr):
			earr.append([cln[n][0],cln[n][1]])
	
	stack=[]
	for n in cln[lvsr+1]:
		stack.append(n)
		if len(stack)>1:
			for i in carr:
				if str(stack[len(stack)-2]) + str(stack[len(stack)-1]) == i[0] or str(stack[len(stack)-2]) + str(stack[len(stack)-1]) == i[1]:
					del stack[len(stack)-1]
					del stack[len(stack)-1]
					stack.append(i[2])
			for i in earr:
				if i[0] in stack and i[1] in stack:
					stack=[]
	
	res.append(stack)

for n in range(len(res)):

	if len(res[n])>0:
		torts = "["
		for i in range(len(res[n])-1):
			torts = torts + res[n][i] + ", "
		torts = torts[:-2] + "]"
	else:
		torts = "[]"
	res[n] = "Case #" + str(n+1) + ": " + torts + "\n"
	
tostr = ""
for n in res:
	tostr+=n
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])