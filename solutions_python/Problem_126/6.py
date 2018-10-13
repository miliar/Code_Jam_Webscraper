#!/usr/bin/env pypy
from cj import jam

def read(reader):
	return reader(str, int)

# def count_cons(s):
# 	n, m = 0, 0
# 	last_cons = True
# 	for c in s:
# 		is_cons = c not in 'aeiou'
# 		if last_cons:
# 			if is_cons:
# 				n += 1
# 			else:
# 				if n > m:
# 					m = n
# 				n = 0
# 		else:
# 			if is_cons:
# 				n = 1
# 		last_cons = is_cons
# 	if n > m:
# 		m = n
# 	return m

# def solve0(s, n):
# 	L = len(s)
# 	v = 0
# 	for i in xrange(L):
# 		for j in xrange(i + 1, L + 1):
# 			ss = s[i:j]
# 			cons = count_cons(ss)
# 			if cons >= n:
# 				v += 1
# 	return v

def solve(s, n):
	cons = []
	last = 0
	last_cons = False
	for c in s:
		is_cons = c not in 'aeiou'
		if is_cons:
			if last_cons:
				last += 1
			else:
				last = 1
		else:
			last = 0
		cons.append(last)
		last_cons = is_cons

	L = len(s)
	v = [0 for _ in xrange(L)]
	for i in xrange(n - 1, L):
		is_cons = s[i] not in 'aeiou'
		v[i] = v[i - 1]
		if is_cons:
			if cons[i] > n:
				v[i] += 1
			if cons[i] == n:
				v[i] = i - n + 2
	return sum(v)

jam(read, solve)
