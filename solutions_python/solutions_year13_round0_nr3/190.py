# Fair and square: http://oeis.org/A057136

# Root of fair and square: http://oeis.org/A057135
# 'also palindromes whose sum of squares of digits is less than 10'
# Let's count these!
# count(A057136 up to X) = count(A057135 up to floor(sqrt(X)))

# X is always strictly positive in the Code Jam problem, so let's drop zero.
# 1 digit: 1, 2, 3
# 2n digits for n>0:
#     2000...0002,
#     1???...???1 with 2, 4, 6 or 8 ones and the rest zeros
# 2n+1 digits for n>0:
#     2000...0002,
#     2000...00100...0002,
#     1???...??2??...???1 with 1 two, 2 or 4 ones and the rest zeros,
#     1???...???1 with 2 to 9 ones and the rest zeros
# Of course, all numbers must be palindromes.

# count(1 digit) = 3
# count(2n digits for n>0) = 1 + (n-1 choose 0) + (n-1 choose 1) + (n-1 choose 2) + (n-1 choose 3)
# count(2n+1 digits for n>0) = 2 + (n-1 choose 0) + (n-1 choose 1)
#                            + ((n-1 choose 0) + (n-1 choose 1) + (n-1 choose 2) + (n-1 choose 3)) for the symmetric ones
#                            * 2 for the choice of the middle digit

from itertools import combinations

def sqrt(n):
	lo, hi = 0, n
	while lo < hi:
		mi = lo + hi + 1 >> 1
		if mi * mi > n:
			hi = mi - 1
		else:
			lo = mi
	assert lo == hi
	return lo

def extra(x, odd):
	'''extra(x, odd) -> twos_increment, ones_full'''
	s = str(x)
	middle = len(s) >> 1
	if s[0] > '2':
		return 1 + odd, True
	elif s[0] == '2':
		# Partial twos. Or not?
		for c in s[1:middle]:
			if c > '0':
				return 1 + odd, True
		if odd and s[middle] > '1':
			return 2, True
		one = odd and s[middle] == '1'
		for c in s[middle+odd:-1]:
			if c > '0':
				return 1 + one, True
		if s[-1] >= '2':
			return 1 + one, True
		return one, True
	else:
		# No twos. Partial ones, or not
		zeros, leading_zeros, leading = 0, 0, True
		for c in s[1:min(4, middle)]:
			if c > '1':
				if not zeros:
					return 0, True
				leading = False
			elif c == '0':
				zeros += 1
				if leading:
					leading_zeros += 1
			else:
				leading = False
		for c in s[4:middle]:
			if c > '0':
				if not zeros:
					return 0, True
				leading = False
			elif c == '0':
				if leading:
					leading_zeros += 1
			else:
				leading = False
		if odd and not zeros and s[middle] > '2':
			return 0, True
		assert False
		return 0, False

def count(x):
	if x < 3:
		return x
	count, hi, odd, n = 3, 100, False, 1
	while hi <= x:
		# These formulae are simplified
		if odd:
			odd = False
			count += 2 + (11 + (n - 3) * n) * n // 3
			n += 1
		else:
			odd = True
			count += 1 + (8 + (n - 3) * n) * n // 6
		hi *= 10
	# incr, ones = extra(x, odd)
	# if ones:
	# 	if odd:
	# 		count += (11 + (n - 3) * n) * n // 3
	# 	else:
	# 		count += (8 + (n - 3) * n) * n // 6
	# return count + incr
	if odd:
		if int('2' + (n - 1) * '0' + '1' + (n - 1) * '0' + '2') <= x:
			count += 2
		elif int('2' + (2 * n - 1) * '0' + '2') <= x:
			count += 1
		count += (11 + (n - 3) * n) * n // 3
		base = '1' + (2 * n - 1) * '0' + '1'
		for k in xrange(4):
			for indices in combinations(xrange(1, n), k):
				s = list(base)
				for i in indices:
					s[i] = s[2 * n - i] = '1'
				if k <= 1:
					s[n] = '2'
					if int(''.join(s)) <= x:
						break
					count -= 1
				s[n] = '1'
				if int(''.join(s)) <= x:
					break
				count -= 1
				s[n] = '0'
				if int(''.join(s)) <= x:
					break
				count -= 1
	else:
		if int('2' + 2 * (n - 1) * '0' + '2') <= x:
			count += 1
		count += (8 + (n - 3) * n) * n // 6
		base = '1' + 2 * (n - 1) * '0' + '1'
		for k in xrange(4):
			for indices in combinations(xrange(1, n), k):
				s = list(base)
				for i in indices:
					s[i] = s[2 * n - 1 - i] = '1'
				if int(''.join(s)) <= x:
					break
				count -= 1
	return count

T = int(raw_input())
for iT in xrange(1, T+1):
	A, B = map(int, raw_input().split())
	print 'Case #%d: %d' % (iT, count(sqrt(B)) - count(sqrt(A - 1)))
