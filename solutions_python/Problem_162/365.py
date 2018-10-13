K = [9,10,1,2,3,4,5,6,7,8]
D = [-1]*1000001

def initD():
	D[0], D[1] = 1,1
	
	for i in xrange(2,len(D)):
		istr = str(i)
				
		ri = long(istr[::-1])
		ristr = str(ri)
		
		if len(istr) == len(ristr) and ri < i and D[i-1] > D[ri]:
			D[i] = D[ri]+1
		else:
			D[i] = D[i-1]+1
			
		# print D[i]

def answer():
	N = long(raw_input())
	cnt = 1
	"""
	while N != 1L:
		
		if len(Nstr) == len(rNstr) and rN < N-1:
			N = rN
			cnt += 1
		else:
			first_n = N%10
			cnt += K[first_n]
			N -= K[first_n]
		# print N
	"""
	return D[N]
	

def main():
	initD()
	for i in xrange(input()):
		print "Case #%d: %d"%(i+1, answer())


if __name__ == "__main__":
	
	main()