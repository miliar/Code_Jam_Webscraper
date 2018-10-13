import itertools, sys;

def createSet(aset):
	for r in range(len(aset)+1):
		for x in itertools.combinations(aset, r):
			for y in itertools.combinations(aset, r):
				if cmp(sorted(x),sorted(y)) != 0:
					yield x, y
	yield None
			
f = open("C:\\jam\\C-small-attempt2.in")
tests = f.readline()
for x in range(0, int(tests)):
	cases = f.readline()[0:-1].split(" ")
	cases.pop(0)
	cases = [int(a) for a in cases]
	it = createSet(cases)
	try:
		while True:
			z, y = next(it)
			if sum(z) == sum(y):
				print "Case #" + str(x+1) + ":"
				for i in range(len(z)):
					sys.stdout.write(str(z[i]) + " ")
				print ""
				for i in range(len(y)):
					sys.stdout.write(str(y[i]) + " ")
				print ""
				break
	except StopIteration:
		print "Case #" + str(x+1) + ":"
		print "Impossible"
		pass

	
	