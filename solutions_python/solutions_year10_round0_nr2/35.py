import sys
import time

try:
	import psyco
	psyco.full()
except ImportError:
	pass

class tee: 
	def __init__(self, *fds):
		self._fds = fds
	
	def write(self, data):
		for fd in self._fds:
			fd.write(data)

	def flush(self):
		for fd in self._fds:
			fd.flush()
	
	def close(self):
		for fd in self._fds:
			fd.close()
	

def fileCaseReader(source):
	entryCount = int(source.readline().strip())
	for i in range(1, entryCount + 1):
		yield i

def readLines(source):
	entryCount = int(source.readline().strip())
	for i in range(0, entryCount):
		yield source.readline()

def readLineOfInts(f):
	return map(int, f.readline().strip().split(" "))
	
def gcd(a,b):
	while b > 0:
		a,b = b, a%b
	return a
		
def runCase(f):
	values = readLineOfInts(f)
	values = values[1:]
	diffs = []
	for i in range(1, len(values)):
		diffs.append(abs(values[i] - values[i - 1]))
	diffGcd = reduce(gcd, diffs)
	result = diffGcd - min(values) % diffGcd
	if result == diffGcd:
		result = 0
	print result

def timerWrap(f):
	def __inner(*args,**kwargs):
		start = time.time()
		try:
			return f(*args, **kwargs)
		finally:
			print >> sys.stderr, "Runtime: %.3f sec" % (time.time() - start)
	return __inner

#@timerWrap
def main():
	f = file("warning.in", "r");
	sys.stdout = tee(sys.stdout, file("warning.out", "w"))
	for index in fileCaseReader(f):
		print "Case #%d:" % index,
		runCase(f)
		sys.stdout.flush()

main()
