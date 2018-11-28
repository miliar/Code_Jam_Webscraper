import sys

class Snapper:
	def __init__(self, has_power=False, state=False):
		self.has_power = has_power
		self.state = state
	def snap(self):
		if self.has_power:
			self.state = not self.state
	def update_power(self, parent):
		if parent.has_power and parent.state:
			self.has_power = True
		else:
			self.has_power = False
	def __str__(self):
		return "has_power: {0}, state:{1}".format(self.has_power, self.state)
 
def snapper_chain(size):
	return [Snapper(True, False)] + [Snapper() for i in range(1, size)]

def snap(chain):
	for snapper in chain:
		snapper.snap()
	for i in range(1, len(chain)):
		chain[i].update_power(chain[i-1])

def print_list(l):
	for o in l:
		print o

def is_light_bulb_on(chain):
	return chain[-1].has_power and chain[-1].state

def test_input(nb_snappers, nb_snaps):
	chain = snapper_chain(nb_snappers)
	for i in range(0, nb_snaps):
		snap(chain)
	return is_light_bulb_on(chain)

def main(argv):
	f = file(argv[0])
	nb_lines = int(f.readline())
	for i in range(0, nb_lines):
		sp = f.readline().split(' ')
		result = test_input(int(sp[0]), int(sp[1]))
		print 'Case #{0}: {1}'.format(i+1, 'ON' if result else 'OFF')
	
		
if __name__ == "__main__":
	main(sys.argv[1:])
