import sys
import time
import re

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
		
def isWinning(a,b):
	a,b=max(a,b),min(a,b)
	if a == b or a == 0 or b == 0:
		return False
	if a >= 2 * b:
		return True
	else:
		return not isWinning(b, a-b)

def runCase(f):
	A1,A2,B1,B2 = readLineOfInts(f)
	s = 0
	for i in range(A1,A2+1):
		for j in range(B1,B2+1):
			if isWinning(i,j):
				s += 1
	print s

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
	f = file("number.in", "r");
	sys.stdout = tee(sys.stdout, file("number.out", "w"))
	for index in fileCaseReader(f):
		print "Case #%d:" % index,
		runCase(f)
		sys.stdout.flush()

main()
