
f = open('palindrome.txt', 'r')

count = int(f.readline().strip())


def check_palindrome(n):
	r = str(n)
	i, j = 0, len(r) - 1
	while i <= j:
		if r[i] != r[j]:
			return False
		i += 1
		j -= 1
	return True


import math

def find_all_fair_square(A, B):
	all_ans = []
	next_seed = int(math.ceil(math.sqrt(A)))
	next = None
	while True:
		if check_palindrome(next_seed):
			next = next_seed ** 2
			if next and next > B:
				break
			if check_palindrome(next):
				all_ans.append(next)		
		next_seed += 1

	return all_ans


for c in range(count):
	[A, B] = [int(i) for i in f.readline().strip().split()]
	ans = find_all_fair_square(A, B)
	print "Case #%d: %d" %  (c + 1, len(ans))
