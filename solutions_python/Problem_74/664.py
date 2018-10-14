import sys, re


class Event():
	def __init__(self, name_, index_):
		self.name = name_
		self.index = index_
	def __str__(self):
		return "%s%s"%(self.name, self.index)
	def __repr__(self):
		return "%s%s"%(self.name, self.index)

class Bot():
	def __init__(self, name_, events_, bots_):
		self.name = name_
		self.events = events_
		self.pos = 1
		self.event_idx = 0
		self.blocked = False
		self.bots = bots_
		self.dest = 1
		seenother = False
		self.signalled = False
		for event in events_:
			if event.name == self.name:
				self.dest = event.index
				break
			elif not seenother:
				seenother = True
				self.blocked = True
		print "Bot", self.name, "created -- blocked: ", self.blocked, "dest: ", self.dest
		
	def process(self):

		if self.event_idx == len(self.events):
			return True
		next_event = self.events[self.event_idx]
		if self.pos != self.dest:
			dir = (self.dest - self.pos)/abs(self.dest - self.pos)
			print "Bot", self.name, "at", self.pos, "moving", dir, "towards", self.dest
			self.pos += dir
		elif next_event.name == self.name and not self.signalled:
			print "Bot", self.name, "pushing button", self.pos
			for bot in self.bots:
				bot.signal(Event(self.name, self.pos))
#		if self.signalled:
#			self.event_idx += 1
#			self.signalled = False

		if self.event_idx == len(self.events):
			return True
			
	def signal(self, event):
		self.signalled = True
		if event.name == self.name:
			self.event_idx += 1
		else:
			my_event = self.events[self.event_idx]
			if my_event.name != event.name or my_event.index != event.index:
				print "Bot", self.name, "got event it was not prepared for?", self.event_idx
				self.event_idx += 1
			else:
				#pass
				self.event_idx += 1
				#Find next destination
		for event in self.events[self.event_idx:]:
			if event.name == self.name:
				self.dest = event.index
				break			

	
def do_line(line, num):
	s = line.split(' ')
	num_, buttons = int(s[0]), s[1:]
	events = []
	for i in range(0,len(buttons), 2):
		events.append(Event(buttons[i], int(buttons[i+1])))
	print events
	bots = []
	bots.append(Bot('B', events, bots))
	bots.append(Bot('O', events, bots))
	
	count = 0
	done = False
	while not done:
		print "Step", count
		for bot in bots:
			if bot.process():
				done = True
		for bot in bots:
			bot.signalled = False
		count += 1
	print "Case #%d: %d" % (num, count)
	out.write("Case #%d: %d\n" % (num, count))


in_, out_f= sys.argv[1], sys.argv[1]+".out"
out = open(out_f, 'w')
with open(in_, 'r') as file:
	file.next()
	num = 1
	for line in file:
		do_line(line, num)
		num += 1
