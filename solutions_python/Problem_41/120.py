input = open('nextnumb.txt', 'r')
output = open('nextnumbans.txt', 'w')

def increm (s):
	i = 0
	while 1:
		i += 1
		if i == len(s):
			s = [0] + s
		if s[-i] > s[-(i+1)]:
			for j in xrange(1, i+1):
				if s[-j] > s[-(i+1)]:
					buf = s[-j]
					s[-j] = s[-(i+1)]
					s[-(i+1)] = buf
					break
			break
	decrem (s, i)
	return s


def decrem (s, a):
	s1 = s[-a:]
	s1.sort()
	s[-a:] = s1
	return s

T = input.readline()
for t in xrange(int(T)):
	mas = []
	N = input.readline()
	if N[-1] == '\n':
		N = N[:-1]
	for j in xrange(len(N)):
		mas.append(int(N[j]))
	ans = increm (mas)
	ans = map(str, ans)
	output.write('Case #' + str(t+1) + ': ' + ''.join (ans) + '\n')

input.close()
output.close()