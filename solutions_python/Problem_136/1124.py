import sys

def q1():
	f = open(sys.argv[1], 'r')
	solve(f)

def readProblem(in_) :
	line = in_.readline()
	split = line.split(' ')
	ret = list()
	for i in split:
		ret.append(float(i))
	return ret
	
def solve(inputFile):
	line = inputFile.readline()
	test_number = int(line)
	#print test_number
	for i in range(1, test_number  +1):
		first = readProblem(inputFile)
		C = first[0]
		F = first[1]
		X = first[2]	
		s = 0.0
		count = 0.0
		N = 0
		#print C, F, X, s, count
		
		while count < X:
			s = s + C / ( N * F + 2 )
			not_buy = (X - C)/(N*F+2) 
			N = N + 1
			if ( not_buy < (X) / ( N * F + 2 ) ):
				s = s + not_buy
				break
		
				
			#print C, F, X, s, N, not_buy
		str_ = "{0:.7f}".format(s)
		print "Case #" + str(i) + ": "+ str_
		
		
		
q1()
		
		
			
			
		
	
		

