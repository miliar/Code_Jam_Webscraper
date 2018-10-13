#dynamic programming

Inf = 1E+5000

def detect(input, n):
	for i in range(n-1,-1,-1):
		if input[i]=='1':
			return i
	return -1

def finish(array, n):
	done = True
	for i in range(0, n):
		if array[i]>i:
			done=False
			break
	return done
	
def solve(array, n):
	step = 0
	for i in range(0,n):
		if array[i]>i:
			#search the nearest move up
			for j in range(i+1,n):
				if array[j]<=i:
					#move
					#print 'Switch', i+1, j+1
					step += j-i
					val = array[j]
					for k in range(j,i,-1):
						array[k]=array[k-1]
					array[i]=val
					#print array
					break
	return step
	
if __name__ == '__main__':
	INFILE = 'A-large.in'
	IN = open(INFILE)
	LINE = IN.readline()
	T = int(LINE) #number of tests
	
	for i in range(T):
		LINE = IN.readline()
		DATA = LINE.split()
		N = int(DATA[0])
		ARRAY = [0]*N
		for j in range(N): #N lines
			LINE = IN.readline()
			POS = detect(LINE, N)
			ARRAY[j] = POS
		ans = solve(ARRAY, N)
		
		print 'Case #%d: %d'%(i+1, ans)
