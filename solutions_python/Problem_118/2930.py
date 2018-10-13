import sys, math

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

f = open(sys.argv[1])
if f != None:
	T = int(f.readline())
	for t in range(1, T+1):
		A, B = map(int, f.readline().split())
		inicio, fim, count = int(math.ceil(math.sqrt(A))), int(math.floor(math.sqrt(B))), 0
		#print inicio, fim
		for i in range(inicio, fim + 1):
			if is_palindrome(i*i) and is_palindrome(i):
				#print i, i*i
				count += 1
		print "Case #%d:" % t, count