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
	
	ils = int(cln[0])
	oloc = 1
	bloc = 1
	
	mc = 0
	bk = 0
	po = 1
	
	while bk==0:
		if po==len(cln):
			break
		
		nom=-1
		nob=-1
		
		for i in range(po,2*ils,2):
			if cln[i] == "O":
				nom = i
				break
		
		for i in range(po,2*ils,2):
			if cln[i] == "B":
				nob = i
				break
		
		if nom == -1 and nob != -1:
			if int(cln[nob+1]) != bloc:
					if int(cln[nob+1])>bloc:
						bloc+=1
					else:
						bloc-=1
			else:
				po+=2
		elif nom != -1 and nob == -1:
			if int(cln[nom+1]) != oloc:
				if int(cln[nom+1])>oloc:
					oloc+=1
				else:
					oloc-=1
			else:
				po+=2
		else:
			if nom<nob:
				if int(cln[nom+1]) != oloc:
					if int(cln[nom+1])>oloc:
						oloc+=1
					else:
						oloc-=1
				else:
					po+=2
					
				if int(cln[nob+1]) != bloc:
					if int(cln[nob+1])>bloc:
						bloc+=1
					else:
						bloc-=1
			else:
				if int(cln[nob+1]) != bloc:
					if int(cln[nob+1])>bloc:
						bloc+=1
					else:
						bloc-=1
				else:
					po+=2
					
				if int(cln[nom+1]) != oloc:
					if int(cln[nom+1])>oloc:
						oloc+=1
					else:
						oloc-=1		
		print(oloc,bloc)
		mc+=1
	
	res.append(mc)

for n in range(len(res)):
	res[n] = "Case #" + str(n+1) + ": " + str(res[n]) + "\n"
	
tostr = ""
for n in res:
	tostr+=n
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])

a=input("Output printed to file!")