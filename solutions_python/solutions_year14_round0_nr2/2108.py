def findN(C, F, X):

	n = 0
	while (X/(2+ n*F) >= (C/(2 + n*F) + X/(2 + (n+1)*F))):
		n += 1
	
	return n

def computeTime(n, C, F, X):

	time = 0
	if n == 0:
		return X/2
	for i in range(n):
		add = C/(2 + (i)*F)
		#print add
		time += add
		if (i+1 ==n):
			time += X/(2 + (i+1)*F)
	return time

	
def main():
	f = open('B-large.in', 'r')
	f2 = open('answer.txt', 'w')
	a = f.readline()
	numtest = int(a[:len(a)-1])
	for i in range(numtest):
		input = f.readline()
		input = input[:len(input)-1]
		input = input.split(' ')
		input = [float(each) for each in input]
		numBuilding = findN(input[0], input[1], input[2])
		a = computeTime(numBuilding, input[0], input[1], input[2])
		a = "Case #" + str(i+1) + ": " + str(a)
		#print a
		f2.write(a)
		if i != numtest-1:
			f2.write('\n')
			
		
		