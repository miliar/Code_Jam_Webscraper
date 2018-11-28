def execute():
	filename = 'B-large.in'
	fp = open(filename,"r")
	noc = int(fp.readline())
	caseno=1
	for x in range(noc):
		ans = [[] for i in xrange(2)]
		case = [int(x) for x in fp.readline().strip().split()]
		n = case[0]
		s = case[1]
		p = case[2]
		case = case[3:]
		ctr = 0
		one = [ [0 for j in range(3)] for i in range(n) ] 
		two = [ [0 for j in range(3)] for i in range(n) ] 
		ans[0]=one
		ans[1]=two
		nos = 0
		nnos = 0
		max_num = 0
		for i in case:
			mod = i%3
			item = i/3
			if mod is 0:
				ans[0][ctr]=[item,item,item]
				if i is 0:
					ans[1][ctr]=[item,item,item]
				else:
					if(item-1>=0 and item+1<=10):
						ans[1][ctr]=[item-1,item,item+1]
						ans[1][ctr].sort(reverse=True)
						nos=nos+1
					else:
						ans[1][ctr]=[item,item,item]
				
			else:
				if(i-item-item-1>=0 and item+1<=10 and i-item-item-1<=10):
					ans[0][ctr]=[item,item+1,i-item-item-1]
					ans[0][ctr].sort(reverse=True)
				if(i-item-item-2>=0 and i-item-item-2<=10):
					ans[1][ctr]=[item+1,item+1,i-item-item-2]
					if((max(ans[1][ctr])- min(ans[1][ctr]))==2):
						nos=nos+1
					else:
						if(i-item-item>=0 and i-item-item<=10):
							ans[1][ctr]=[item,item,i-item-item]
							if((max(ans[1][ctr])-min(ans[1][ctr]))==2):
								nos=nos+1
						else:
							ans[1][ctr]=ans[0][ctr]
				elif(i-item-item>=0 and i-item-item<=10):
					ans[1][ctr]=[item,item,i-item-item]
					if((max(ans[1][ctr])-min(ans[1][ctr]))==2):
						nos=nos+1
					else:
						ans[1][ctr]=ans[0][ctr]
						
				ans[1][ctr].sort(reverse=True)
			ctr = ctr+1
		#print ans
		#print "n=%d s=%d nos=%d p=%d" %(n,s,nos,p)
		if s==0:
			for i in ans[0]:
				for j in i:
					if (j >= p):
						max_num=max_num+1
						break
		elif s==n:
			for i in ans[1]:
				for j in i:
					if (j >= p):
						max_num=max_num+1
						break
		
		else:
			nnos=0
			ctr=0
			temp=[]
			for i in ans[0]:
				flag=0
				for j in i:
					if(j >= p):
						max_num= max_num+ 1
						flag=1
						temp.append(ctr)
						break
				if(flag is 0):
					if(nnos<s):
						if((max(ans[1][ctr])-min(ans[1][ctr]))==2):
							for j in ans[1][ctr]:
								if(j>=p):
									max_num=max_num+1
									nnos = nnos + 1
				ctr = ctr + 1
			if(nnos<s):
				for i in temp:
					if((max(ans[1][i])-min(ans[1][i]))==2):
						for j in ans[1][i]:
							if(j>=p):
								nnos = nnos + 1
								break
					if(nnos==s):
						break
			#print "max_num=%d "%(max_num)
		#print "nnos=%d"%(nnos)		
		print "Case #%d: %d" %(caseno,max_num)
		caseno = caseno+1
		#print ans
		
if __name__=='__main__':
	execute()