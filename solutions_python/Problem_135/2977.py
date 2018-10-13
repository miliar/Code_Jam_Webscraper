class PeekReader(object):
	def __init__(self, source):
		self.source = source
		self.nextline = None

	def _popcache(self):
		nextline = self.nextline
		self.nextline = None
		return nextline

	def _pushcache(self):
		self.nextline = self.source.readline()
		return self.nextline

	def readline(self):
		line = self.source.readline() if self.nextline is None else self._popcache()
		if not line: raise EOFError()
		return line

	def readline_num(self):
		return int(self.source.readline())

	def peekline(self):
		line = self._pushcache() if self.nextline is None else self.nextline
		if not line: raise EOFError()
		return line

def question():
	choice = stdin.readline_num()
	grid = [stdin.readline() for i in xrange(4)]
	return set( map(int, grid[choice-1].split(' ')) )

def main():
	casenums = stdin.readline_num()
	for casenum in xrange(1,casenums+1):
		q1 = question()
		q2 = question()
		intersect = q1 & q2
		if len(intersect) == 0:
			msg = "Volunteer cheated!"
		elif len(intersect) == 1:
			msg = next(iter(intersect))
		else:
			msg = "Bad magician!"
		print 'Case #%d: %s' % (casenum, msg)

if __name__ == '__main__':
	from sys import stdin as raw_stdin
	stdin = PeekReader(raw_stdin)
	main()
