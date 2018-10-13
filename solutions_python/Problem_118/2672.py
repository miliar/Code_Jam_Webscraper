import math
import sys

def palindromes(L):
	return filter(palindrome, L)

def palindrome(L):
	L = str(L)
	return L == L[::-1]

def perfect_squares(mini, maxi):
  lowest = int(math.ceil(math.sqrt(mini)))
  highest = int(math.sqrt(maxi))
  return [n**2 for n in range(lowest, highest + 1)]

num_cases = int(sys.stdin.next())
#print num_cases
for i in range(num_cases):
	(a,b) = sys.stdin.next().split(' ')
	#print palindromes(perfect_squares(int(a),int(b)))
	lst = map(int,map(math.sqrt,palindromes(perfect_squares(int(a),int(b)))))
	#print lst
	#print 'Case #%d: %d' % (i+1, len(palindromes(perfect_squares(int(a),int(b)))))
	print 'Case #%d: %d' % (i+1, len(palindromes(lst)))