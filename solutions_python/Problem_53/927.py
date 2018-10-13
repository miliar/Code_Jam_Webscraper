import sys

def readinputs():
	return list(map(int, sys.stdin.readline().strip().split(' ')))

class Snapper(object):
	is_on = False
	is_plugged = False
	is_first = False
		
	def __init__(self, is_on=False, is_plugged=False, is_first=False):
		self.is_on = is_on
		self.is_plugged = is_plugged
		self.is_plugged = is_plugged
		self.is_first = is_first
	
	def snap(self):
		if self.is_plugged or self.is_first:
			if self.is_on:
				self.is_on = False
			else:
				self.is_on = True
	
	def on_or_off(self):
		if self.is_on and self.is_plugged:
			return "ON"
		else:
			return "OFF"

if __name__ == "__main__":
	T = readinputs()[0]
	case = 1
	for _ in xrange(T):
		N, K = readinputs()
	
		snappers = []
		for i in xrange(N):
			snappers.append(Snapper())
		snappers[0].is_plugged = True
		snappers[0].is_first = True
		
		for i in xrange(K):
			last = snappers[0]
			for snapper in snappers:
				snapper.snap()
				
				if not snapper.is_first:
					snapper.is_plugged = (last.is_on and last.is_plugged)
				
				last = snapper
				
		print "Case #%d: %s" % (case, snappers[-1].on_or_off())
		case = case + 1
		