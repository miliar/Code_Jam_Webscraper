import sys

infile="A-large.in"

outfile=""
outfile=infile+".out"

def main():
	fi=open(infile, "r")
	if outfile != "":
		fo=open(outfile, "w")
	else:
		fo = sys.stdout

	def pout(*args, end="\n"):
		print(*args, file=fo, end=end)

	T=int(fi.readline()[:-1])
	for test in range(T):
	
		mat=[]
		N=int(fi.readline()[:-1])
		for num in range(N):
			a = fi.readline()[:-1]
			try:
				n = a.rindex('1')
			except:
				n=0
			mat.append(n)
			
		print(mat)
		K=0
		for i in range(N):
			p=0
			for j in range(i,N):
				if mat[j] <= i:
					p=j
					break
			K += p-i
			tmp=mat[i:p]
			mat[i]=mat[p]
			mat[i+1:p+1]=tmp
#			print(mat,K)
		
		pout("Case #{0}: {1}".format(test+1,K))


if __name__ == '__main__':
	main()
