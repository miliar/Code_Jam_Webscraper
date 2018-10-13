from decimal import Decimal

def is_ok(t, D, horses):

	v = float(D/t)


	m = list()
	for horse in horses:

		v = horse[-1]
		x = horse[-2]
	
		f_x = x + v*t

		m.append(Decimal(f_x-D))

	return min(m)




def solve(horses, D):

	li = 0
	ls = D

	ok = False

	tr = list()

	while ok is False:
		t = float((li + ls)/2)

		t = round(t, 6)

		if t in tr:
			return float(D/t)
		else:
			tr.append(t)

		m = is_ok(t, D, horses)

		if m == Decimal(0.0):
			ok = True
			return float(D/t)
		elif m > 0.0:
			ls = t
		elif m < 0.0:
			li = t


def main():  

	T = int(raw_input())
	responses = dict()
	for t in xrange(1, T+1):

		D, N = map(int, raw_input().split())

		D = float(D)
		
		horses = list()
		for n in range(N):
			horses.append(map(float,raw_input().split()))

		vel = solve(horses, D)

		responses[t] = vel

	for t in xrange(1, T+1):

		print "Case #%d: %f" % (t, responses[t])





if __name__ == "__main__":
	main()

'''
2
1000000000 1
999999999 1
1000000000 1
1 1


1
1000000000 2
999999996 3
999999997 2

'''