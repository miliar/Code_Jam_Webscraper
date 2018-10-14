import sys

class Snapper:
	pass

def snap(snappers):
	# toggle all powered snappers
	for i in range(0, len(snappers)):
		if snappers[i].powered:
			snappers[i].on = not snappers[i].on
			
	# determine which snappers are powered now
	for i in range(1, len(snappers)):
		snappers[i].powered = snappers[i - 1].on and snappers[i - 1].powered
	
def main(argv):
	F = open(argv[1], "r")
	
	T = int(F.readline())
	
	for t in range(0, T):
		(N, K) = [int(d) for d in F.readline().split()]
		
		# init snappers
		snappers = []
		for i in range(0, N):
			s = Snapper()
			s.powered = False
			s.on = False
			snappers.append(s)
		snappers[0].powered = True # first snapper connected to power source
		
		# snap times
		for i in range(0, K):
			snap(snappers)
		
		light_state = "OFF"
		if snappers[-1].on and snappers[-1].powered:
			light_state = "ON"
		
		print "Case #%d: %s" % (t + 1, light_state)
	
if __name__ == "__main__":
	main(sys.argv)