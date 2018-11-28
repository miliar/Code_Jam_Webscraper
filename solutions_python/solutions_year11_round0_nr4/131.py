filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

res = []

for n in range(2,ls*2+1,2):
	print(n)
	cln = ipt[n]
	cln = cln.split(" ")
	
	for i in range(len(cln)):
		cln[i] = int(cln[i])

	sum = 0
	s = sorted(cln)
	for i in range(len(cln)):
		if cln[i] != s[i]:
			sum+=1
	
	res.append(sum)
	
tostr = ""
for n in range(len(res)):
	tostr+="Case #" + str(n+1) + ": " + str(res[n]) + ".000000" + "\n"
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])
s=input("Die Zeit ist um.")
	