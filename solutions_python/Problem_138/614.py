from sys import stdin

def go1(a, b):
	a = list(a)
	b = list(b)

	a.sort(key = lambda x : -x)
	b.sort(key = lambda x : -x)

	score = 0
	while a:
		aa = a.pop(0)
		while b:
			bb = b.pop(0)
			if aa > bb:
				score += 1
				break

	return score

def go2(a, b):
	a.sort(key = lambda x : -x)
	b.sort()

	score = 0
	while a:
		aa = a.pop(0)
		for bb in b:
			if bb > aa:
				b.remove(bb)
				break
		if len(a) != len(b):
			score += 1
			b.pop(0)
	return score



T = int(stdin.readline())

for z in range(1, T+1):
	n = int(stdin.readline())
	a = [float(x) for x in stdin.readline().split()]
	b = [float(x) for x in stdin.readline().split()]

	print 'Case #' + str(z)+':', go1(a, b), go2(a, b)