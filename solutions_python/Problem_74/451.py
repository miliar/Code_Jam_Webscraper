import os

def read_vector(s):
	return [i for i in s.split(" ")]

filepath = "/home/mike/Downloads/"
filename = "A-large"

f_in = open(os.path.join(filepath, filename+".in"), "rb")
f_out = open(os.path.join(filepath, filename+".out"), "wb")
num_test_cases = int(f_in.readline())

DEBUG = False

def debug(s):
	if DEBUG: print s

class Bot(object):
	def __init__(self):
		self.button = {'O':[], 'B':[]}
		self.pos = {'O':1, 'B':1}
		self.control = []
		self.other = []
	
	def add(self, colour, position):
		self.button[colour].append(position)
		self.control.append(colour)
		self.other.append(('O','B')[colour == 'O'])
		
	def move_control(self):
		if (self.pos[self.control[0]] < self.button[self.control[0]][0]): self.pos[self.control[0]] += 1
		else: self.pos[self.control[0]] += -1
		debug("%s: Move to %d" % (self.control[0], self.pos[self.control[0]]))

	def move_other(self):
		if (self.pos[self.other[0]] < self.button[self.other[0]][0]): self.pos[self.other[0]] += 1
		else: self.pos[self.other[0]] += -1
		debug("%s: Move to %d" % (self.other[0], self.pos[self.other[0]]))
		
	def get_button_control(self):
		return self.button[self.control[0]][0]

	def get_button_other(self):
		return self.button[self.other[0]][0]
	
	def get_control(self):
		return self.control[0]
	
	def get_other(self):
		return self.other[0]
	
	def get_pos_control(self):
		return self.pos[self.control[0]]

	def get_pos_other(self):
		return self.pos[self.other[0]]
	
	def push_button(self):
		debug("%s: Push button %d" % (self.control[0], self.button[self.control[0]][0]))
		self.button[self.control[0]].pop(0)
		self.control.pop(0)
		self.other.pop(0)
		
	def is_done(self):
		return len(self.control) == 0 
		
for test_case in xrange(1, num_test_cases+1):
	bot = Bot()
	
	V = read_vector(f_in.readline())
	N = int(V.pop(0))

	for i in xrange(0, N):
		bot.add(V.pop(0), int(V.pop(0)))
	
	step = 1
	while(True):
		debug("Step %d, " % step,)
		try:
			if (bot.get_pos_other() == bot.get_button_other()): pass
			else: bot.move_other()
		except:
			pass

		if (bot.get_pos_control() == bot.get_button_control()):	
			bot.push_button()
			
		else: bot.move_control()

		if (bot.is_done()): break
		step += 1
		
		
		#if step > 10: break
		
	output = "Case #%d: %d" % (test_case, step)
	print output
	f_out.write(output+"\n")

f_out.close()