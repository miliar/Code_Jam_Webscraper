import sys

def main():
	f=file(sys.argv[1])
	N=int(f.readline())
	I=0
	while N>0:
		I+=1
		N-=1
		Max,nOk,nOl=map(int,f.readline().split())
		ws=map(int,f.readline().split())
		ws=sorted(ws,reverse=True)
		res=0
		for i,n in enumerate(range(0,nOl,nOk)):
			res+=sum(ws[n:n+nOk])*(i+1)	
		"""
		tmp=[[]]*nOk
		for n in range(min(nOk,nOl)):
			tmp[n]=ws[n::nOk]
		tmp=zip(*tmp)
		res=0
		for i,keys in enumerate(tmp):
			res+=sum(keys)*(i+1)
			"""
		print "Case #%d: %d"%(I,res)
if __name__=="__main__":
  main()
