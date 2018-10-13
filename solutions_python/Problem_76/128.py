filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

res = []
for n in range(2,ls*2+1,2):
	print(n)
	cln = ipt[n]
	cln = cln.strip()
	cln = cln.split(" ")
	for i in range(len(cln)):
		cln[i] = int(cln[i])
	cln = sorted(cln)
	a=0
	b=0
	for i in range(1,len(cln)):
		a=a^int(cln[i])
		b=b+int(cln[i])
	print(cln[0])
	if a==int(cln[0]):
		res.append(b)
	else:
		res.append("NO")
		
tostr = ""
for n in range(len(res)):
	tostr+="Case #" + str(n+1) + ": " + str(res[n]) + "\n"
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])
s=input("Die Zeit ist um.")