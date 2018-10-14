import sys

def solve(infname,outfname):
	f = open(infname,'r')
	out = open(outfname,'w')

	T = int(f.readline())
	for t in range(0,T):
		N = int(f.readline())
		strs = []

		for i in range(0,N):
			strs.append(f.readline()[:-1])
		conf = []
		orisymb = ''
		flag = False
		for i in range(0,N):
			symb = ''
			if flag: break
			conf.append([])
			for j in range(0,len(strs[i])):
				if j>0 and strs[i][j]==strs[i][j-1]:
					conf[i][-1]+=1
				else:
					conf[i].append(1)
					symb = symb+strs[i][j]
			if i==0:
				orisymb = symb
			else:
				if not symb==orisymb:
					flag = True
		if flag:
			out.write("Case #%d: Fegla Won\n"%(t+1))
		else:
			cost = 0
			for i in range(0,len(symb)):
				tmp = [conf[j][i] for j in range(0,N)]
				tmp.sort()
				mid = tmp[int(N/2)]							
				tmp1 = [abs(conf[j][i]-mid) for j in range(0,N)]
				cost +=sum(tmp1)
			out.write("Case #%d: %d\n"%(t+1,cost))

	f.close()
	out.close()


if __name__=="__main__":
	solve(sys.argv[1],sys.argv[2])
