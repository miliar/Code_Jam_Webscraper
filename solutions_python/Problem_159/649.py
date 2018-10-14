import fileinput
import pdb

def diff(t):
	return [j-i for i, j in zip(t[:-1], t[1:])] 

def variable(steps):
	total = 0
	for i in xrange(len(steps)-1):
		if steps[i] > steps [i+1]:
			total += (steps[i] - steps[i+1])
	return total

def const(steps):
	total = 0
	di = diff(steps)
	rate = abs(min(di))
	for i in xrange(len(di)):
		if steps[i] < rate:
			total += steps[i]
		elif steps[i] < 1:
			pass
		else:
			total += rate
	return total

T = 0
for line in fileinput.input():
	if T == 0 or T % 2 == 1:
		T += 1
		continue

	steps = [int(x) for x in line.split()]
	ans1 = variable(steps)	
	ans2 = const(steps)
	print "Case #{}: {} {}".format(T/2,ans1, ans2)
	T += 1
