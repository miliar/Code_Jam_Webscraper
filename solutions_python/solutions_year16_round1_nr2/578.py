def soldier(inputfile, outputfile):
	fr=open(inputfile,'r')
	T=int(fr.readline())
	print(T)
	fw=open(outputfile,'w')
	for i in range(T):
		N=int(fr.readline())
		print(N)
		ndict={}
		for j in range(N*2-1):
			nums=[int(s) for s in fr.readline().split(" ")]
			for nm in nums:
				if nm in ndict:
					ndict[nm]=ndict[nm]+1
				else:
					ndict[nm]=1
		result=[]
		for k,v in ndict.items():
			if v%2==1:
				result.append(k)
		result.sort()
		rs='Case #'+str(i+1)+':'
		for x in result:
			rs=rs+' '+str(x)
		rs=rs+'\n'
		fw.write(rs)
		print(rs)
	fw.close
	fr.close
	return
