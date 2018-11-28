#! /usr/bin/python3

def tidy(n):
	p = 48+11
	for i in str(n)[::-1]:
		if ord(i) > p:
			# print(ord(i), p)
			return False
		p = ord(i)
	return True

def f(n):
	i = n
	while i > 9:
		if tidy(i):
			return i
		i -= 1
	return min(i, 9)

def f2(n):
	if tidy(n):
		return n
	s = str(n)
	l = len(s)
	if (n % 10) <= l:
		n -= 10
		n += (10 - n % 10 - 1)
		# print(n)
		t = 10
		# i = 10
		d = (n % t) // (t // 10)
		# print('d', d)
		# d = 9
		while t < n:
			# print((n % (t*10)) // t, d)
			while (n % (t*10)) // t > d:
				n -= t
				print(n)
			d = (n % (t*10)) // t
			t *= 10
			# print(n)
	else:
		t = 10
		d = (n % t) // (t // 10)
		# print('d', d)
		p = 9
		while t < n:
			# print((n % (t*10)) // t, d)
			while (n % (t*10)) // t > d:
				# n -= t * 10
				# n += (t * 10 - (n % ((t*10)) // ) - 1)
				# n -= t
				r = n % (t//10)
				dv = n // t - 1
				n = dv * t + p * t // 10 + r
				print(r, d, n)
				break
				print(n)
			p = d
			d = (n % (t*10)) // t
			t *= 10
	return n

def minus1(s):
	if s:
		n = int(s) - 1
		if n != 0:
			return str(n)
	return ''

def f3(n):
	# if tidy(n):
	# 	return n
	s = str(n)
	while True:
		for i in range(1, len(s)):
			# print(s[i-1], s[i])
			if ord(s[i-1]) > ord(s[i]):
				s = minus1(s[:i]) + '9' * (len(s) - i)
				# print(s)
				# return s
				break
		else:
			break
	return s

# print(f(6468))

t = int(input())
for it in range(1, t+1):
	n = int(input())
	print("Case #%d:" % it, f3(n))
