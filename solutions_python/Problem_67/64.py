import sys
import time
import copy

try:
	import psyco
	psyco.full()
except ImportError:
	pass

class Tee(object): 
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

class InputReader(object):
	def __init__(self, f):
		self.f = f
	
	def readline(self):
		return self.f.readline().strip()
	
	def readnlines(self):
		entryCount = int(self.readline())
		for i in range(0, entryCount):
			yield self.readline()
		
	def readints(self):
		return list(map(int, self.readline().split(" ")))
	
	def readmatrix(self, rows, linetrans=lambda x:x):
		return [linetrans(self.readline()) for i in range(rows)]
	
	def readcases(self):
		entryCount = int(self.readline())
		for i in range(1, entryCount + 1):
			yield i

def timerWrap(func):
	def __inner(*args,**kwargs):
		start = time.time()
		try:
			return func(*args, **kwargs)
		finally:
			sys.stderr.write("Runtime: %.3f sec\n" % (time.time() - start))
	return __inner
	
def dead(field):
	for line in field:
		if 1 in line:
			return False
	return True
	
def cycle(field):
	oldfield = copy.deepcopy(field)
	for y, line in enumerate(field):
		for x, row in enumerate(field):
			if x == 0 or y == 0:	
				field[y][x] = 0
			elif (oldfield[y-1][x] == 1 and oldfield[y][x-1] == 1):
				field[y][x] = 1
			elif (oldfield[y-1][x] == 1 or oldfield[y][x-1] == 1) and (oldfield[y][x] == 1):
				field[y][x] = 1
			else:
				field[y][x] = 0
	return field

def runCase(inpFile):
	R, = inpFile.readints()
	field = [[0] * 100 for i in range(100)]
	for i in range(R):
		X1,Y1,X2,Y2 = inpFile.readints()
		for x in range(X1-1,X2):
			for y in range(Y1-1, Y2):
				field[y][x] = 1
	cnt = 0
	while not dead(field):
		field = cycle(field)
		cnt += 1 
	print (cnt)

#@timerWrap
def main():
	inpFile = InputReader(open("bacteria.in", "r"))
	sys.stdout = Tee(sys.stdout, open("bacteria.out", "w"))
	for index in inpFile.readcases():
		print "Case #%d:" % index, 
		runCase(inpFile)
		sys.stdout.flush()

main()
