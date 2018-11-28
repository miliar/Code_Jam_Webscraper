import sys
import math
import re


palindromes = set()
def find_palindromes(s, i, l):
	#print('s:', s, i)
	if i >= l/2:
		if s[0] != '0':
			palindromes.add(int(''.join(s)))
		#print('a')
		return

	for n in range(10):
		s[i] = s[-i-1] = str(n)
		find_palindromes(s, i+1, l)


def case():

	A, B = [int(x) for x in input().split(' ')]
	
	start = int(math.ceil(A**.5))
	end = int(B**.5)

	#print (start, end)

	count = 0
	for i in palindromes:
		if i > end:
			break

		if i >= start and i*i in palindromes:
			#print (i, ',', i*i)
			count += 1


	sys.stdout.write(str(count))




if __name__=="__main__":

	s = []
	for i in range(3):
		s.append('0')
		find_palindromes(s, 0, len(s));
	palindromes = sorted(palindromes)
	#print(palindromes)

	if len(sys.argv) > 1:
		sys.stdin = open(sys.argv[1])

	num_cases = int(input())

	for c in range (1, num_cases+1):
		sys.stdout.write('Case #')
		sys.stdout.write(str(c))
		sys.stdout.write(': ')
		case()
		sys.stdout.write('\n')
