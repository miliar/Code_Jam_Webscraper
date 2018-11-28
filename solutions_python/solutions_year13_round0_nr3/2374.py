from math import sqrt

def fairAndSquare(number):
	def isPalindrome(entry):
		return entry == entry[::-1]

	if isPalindrome(str(number)):
		root = int(sqrt(number))
		if root * root == number and isPalindrome(str(root)):
			return True
	return False

def amountBetweenTuple(a,b):
	return str(len(filter(lambda x : x, map(fairAndSquare, xrange(a,b+1)))))


def run():
	f = open('C-small.in','r')
	targetAmount = int(f.readline())

	s = ""
	for i in xrange(targetAmount):
		line = f.readline()
		AB = line.replace('\n','').split(' ')
		s = s + "Case #" + str(i+1) + ": " + amountBetweenTuple(int(AB[0]),int(AB[1])) + "\n"
	f.close()

	fw = open('C-small.out','w')
	fw.write(s)
	fw.close

run()

