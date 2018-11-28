n = int(input())
import math

def rep(str, proto=None):
	r = []
	last = str[0]
	count = 0
	for x in str:
		if not x == last:
			r.append((last, count))
			last = x
			count = 1
		else:
			count += 1
	if count > 0:
		r.append((last, count))
	return r

def distanceToX(l, val):
	lower = sum([abs(x - math.floor(val)) for x in l])
	upper = sum([abs(x - math.ceil(val)) for x in l])
	return min(lower, upper)

for u in range(n):
	t = int(input())
	FAIL = False


	reps = []
	r = rep(input())
	chars = [x for x,y in r]
	reps.append([b for a,b in r])
	for x in range(1, t):
		r = rep(input())
		chars2 = [a for a,b in r]
		if not len(chars) == len(chars2):
			FAIL = True
			break
		for a,b in zip(chars, chars2):
			if not a == b:
				FAIL = True
				break

		if FAIL:
			break

		reps.append([b for a,b in r])

	if not FAIL:
		#print ("Reps", reps)
		s = 0
		for x in range(len(chars)):
			values = [z[x] for z in reps]
			mid = sum(values) / float(len(values))
			s += distanceToX(values, mid)

		print ("Case #{}: {}".format(u + 1, s))
	else:
		print ("Case #{}: Fegla Won".format(u + 1))