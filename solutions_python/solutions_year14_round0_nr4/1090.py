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
		line = inputFile.readline()
		hamoi = readProblem(inputFile)
		ken = readProblem(inputFile)
		hamoi.sort()
		ken.sort()

		ohamoi = hamoi[:]
		oken =  ken[:]
		ken_max = oken[len(oken)-1]
		owin = 0
		for j in ohamoi :
			if j < oken[0]:
				oken.pop(len(oken)-1)
			else:
				oken.pop(0)
				owin = owin + 1
			
		k_count = 0
		h_win = 0
		#print hamoi
		#print ken
		for j in hamoi :
			while k_count < len(ken) and ken[k_count] < j:
				k_count = k_count + 1
			if k_count < len(ken) :
				ken.pop(k_count)
				k_count = max( 0 , k_count - 1)
			else:
				ken.pop(0)
				h_win = h_win + 1

		
				
		
		print "Case #" + str(i) + ": "+ str(owin) + " "+ str(h_win)
		
		
		
q1()
		
		
			
			
		
	
		

