import sys

fd = sys.stdin
out = sys.stdout

def copylist(list):
	new = []
	for i in list:
		new.append(i)

	return new

tests = int(fd.readline())

for test in xrange(0, tests):
	change = 0
	engines = []
	searcheng = int(fd.readline())
	for eng in xrange(0, searcheng):
		engines.append(fd.readline())

	copy = copylist(engines)

	querys = int(fd.readline())
	
	for i in xrange(0, querys):
		query = fd.readline()
		try:
			copy.remove(query)
		except ValueError:
			pass

		if len(copy) == 0:
			change += 1
			copy = copylist(engines)
			copy.remove(query)

	out.write('Case #%d: %d\n'% (test+1, change))
