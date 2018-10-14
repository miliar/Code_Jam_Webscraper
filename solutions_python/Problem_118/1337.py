import math

def isPalindrome(string):
	m_len = len(string)
	for i in range(0, m_len/2):
		if string[i] != string[m_len-1-i]:
			return False
	return True

def isSquare(num):
	n = math.sqrt(float(num))
	return n == int(n);


def search_range(m_range):
	cont = 0
	for i in range(m_range[0], m_range[1]+1):
		square = math.sqrt(i)
		if isPalindrome(str(i)) and square == int (square) and isPalindrome("%i"%square):
			#print "found: %i"%i
			cont = cont + 1
	return cont

def main():
	inputFolder = "/home/pabratte/Downloads/"
	input = open(inputFolder+"C-small-attempt0.in")
	nTestCases = int(input.readline())
	for i in range(0, nTestCases):
		m_range = [int(s) for s in input.readline().split() if s.isdigit()]
		print "Case #%i: %i"%(i+1, search_range(m_range))


	input.close()

if __name__ == "__main__":
    main()
