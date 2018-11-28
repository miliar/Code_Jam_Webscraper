from util import *

def to_arr(s):
	arr = 0
	counter = 0
	for z in s:
		arr = arr << 1
		if z == '+':
			arr += 1
			counter += 1
	return arr, counter, len(s)

def p1(s, m):
	s, i, nbit = to_arr(s)
	global n 
	n = nbit

	if m % 2 == 0 and (nbit-i) % 2 != 0:
		return "IMPOSSIBLE"
	if s == (1<<n)-1:
		return 0
	result = BFS(s, m)
	if result is None:
		result = "IMPOSSIBLE"
	return result

def BFS(s, m):
	c = 0
	q = [(s,0)]
	s_set = set()
	while q:
		v,c = q.pop(0)
		for i in range(0, n-m+1):
			t = v ^ (((1<<m)-1) << i)
			if t in s_set:
				continue

			if (1<<n)-1 == t:
				return c+1
			q += [(t, c+1)]
			s_set.add(t)

	return None

########Testing###########

def binary(n):
	s = ""
	while n > 0:
		if n % 2 == 0:
			s = "0" + s
		else:
			s = "1" + s
		n /= 2
	return s

if __name__ == "__main__":
	# print p1("+--+--", 3)
	T = -1
	counter = 0
	while True:
		try:
			if T == -1:
				T = input()
			counter += 1
			args = raw_input()
			s = args.split(' ')[0]
			m = int(args.split(' ')[1])
			print "Case #%d: %s" % (counter, str(p1(s, m)))
		except EOFError:
			break
