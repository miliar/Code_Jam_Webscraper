from sets import Set

def cycle(n):
	cy = []
	number = str(n)
	for i in range(1,len(number)+1):
		cy.append(number[i:]+number[:i])
	return cy

def recycle5(A,B):
	solution = 0	
	length = len(str(A))	
	for i in xrange(A,B):
		current_n = i		
		rota = Set(cycle(i))
		for item in rota:
			item = int(item)
			if item <= B and item > current_n and item >= A:				
				solution +=1
	return solution	

def get_problems():
	f = file("C-large.in")
	f2 = open("C-large.out", 'w')
	numCases = f.readline()
	for i in xrange(1, int(numCases)+1):
		line = f.readline().split()
		output = recycle5(int(line[0]), int(line[1]))	
		stra = "Case #%d: %s" % (i, output)
		print stra		
		f2.write(stra + "\n")
	f2.close()



get_problems()







