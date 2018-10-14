
from copy import deepcopy

if __name__ == '__main__':

	t = int(raw_input()) 
	for k in xrange(1, t + 1):
		raw = raw_input()

		D, N = raw.split(' ')
		D = float(D)
		N = int(N)

		horse = []

		for i in xrange(N):
			pos, speed = raw_input().split(' ')
			horse.append( (float(pos), float(speed)) )

		# print horse
		horse = sorted(horse, key=lambda tup: tup[0])

		time = 0.0

		while len(horse) > 1:

			# print horse

			a, b = horse.pop()
			c, d = horse.pop()

			if b==d :
				horse.append( (c, d) )
				continue

			x = (a-c)/(d-b)
			y = a + b*x

			# print x

			if x >= 0:
				if y <= D:
					time = time + x
					horse.append( (y, min(b,d)) )
				else:
					horse.append( (c, d) )
			else:
				horse.append( (c, d) )

			pass

		# print horse

		time = time + (D-horse[0][0])/horse[0][1]

		result = D/time

		print 'Case #{}: {}'.format(k, result)

