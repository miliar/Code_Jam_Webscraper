# n stalls
# k people
def urinal(n,k):
	nodes = [n]

	s = None

	for i in range(k):
		nodes.sort()
		nodes = nodes[::-1]

		o = nodes.pop(0)
		s = sub(o)
		nodes.append(s[0])
		nodes.append(s[1])

	return s


def sub(x):
	if x == 1:
		return (0,0)
	elif x % 2 == 0:
		return (x/2, x/2-1)
	else:
		return ((x-1)/2, (x-1)/2)


lines = int(raw_input())

for i in range(lines):
	l = raw_input().split(' ')

	n = int(l[0])
	k = int(l[1])

	u = urinal(n,k)

	print('Case #' + str(i+1) + ": " + str(u[0]) + " " + str(u[1]))
