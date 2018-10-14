# Check to see if q->z and z->q OR q->q and z->z !

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

f = file('a.in', 'r')
N = int(f.readline())
for i in range(1, N + 1):
	sentence = f.readline().strip()
	answer = ''
	for j in sentence:
		answer += d[j]
	print 'Case #%d:' % i, answer
