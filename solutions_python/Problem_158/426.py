

def richard_wins(x, r, c):
	if (r*c)%x != 0:
		return True

	if x <= 2:
		return False
	elif x == 3:
		return r==1 or c==1
	elif x == 4:
		return r<=2 or c<=2

	return False

def solve(testid):
	f = open(testid + '.in')
	g = open(testid + '.out', 'w')

	T = int(f.readline())

	for i in range(1,T+1):
		print i
		(x, r, c) = [int(u) for u in f.readline().split()]
		if richard_wins(x, r, c):
			result = "RICHARD"
		else:
			result = "GABRIEL"

		g.write('Case #{}: {}\n'.format(i, result))

	f.close()
	g.close()

if __name__ == '__main__':
#	solve('D-sample')
	solve('D-small-attempt0')
#	solve('D-large')


