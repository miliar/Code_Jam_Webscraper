import sys
from numpy import zeros

def toggle(line):
	n, k = map(int,line.split(' '))
#	print "n:%d k:%d" % (n, k),	
	switches_state = zeros(n)
	num_powered = 1
	for i in xrange(k):
		for j in xrange(0, num_powered):
			switches_state[j] = not switches_state[j]
			num_powered = 1
			for l in xrange(1, len(switches_state)):
				if switches_state[l - 1]:
					num_powered += 1
				else:
					break
#	print "num_powered:%d switches_state: "% (num_powered), switches_state
	if num_powered == n and switches_state[-1]:
		return 'ON'
	else:
		return 'OFF'

in_ = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')

lines = [a for a in in_]

for i,line in enumerate(lines[1:]):
	line.rstrip()
	state = toggle(line)
#	print "Case #%d: %s\n" % (i+1, state)
	out.write("Case #%d: %s\n" % (i+1, state))

