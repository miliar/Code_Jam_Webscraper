#!/usr/bin/env python

class Bot:
	def __init__(self, name, list):
		self.list = list
		self.name = name
		self.atButton = 1
		self.tickcount = 0
		self.justPressed = False
	def tick(self):
		if self.justPressed:
			self.justPressed = False
			return
		try:
			if self.atButton == self.list[0]:
				self.tickcount += 1
				return
			if self.atButton > self.list[0]:
				self.atButton -= 1
			elif self.atButton < self.list[0]:
				self.atButton += 1
			#print self.name, "is now at", self.atButton
		except IndexError:
			#print self.name, "is Done."
			pass
		self.tickcount += 1
	def press(self):
		if self.atButton == self.list[0]:
			#print self.name, "is pushing!", self.tickcount
			self.list.pop(0)
			self.justPressed = True
			self.tickcount += 1
			return True
		#print self.name, "isn't there yet"
		return False
	def done(self):
		if len(self.list) == 0:
			return True
		return False

#Bot Trust

if __name__ == "__main__":
	inf = file("bottrust.in", "r")
	inf.readline()
	cases = []
	for line in inf:
		linelist = line.split(" ")
		newline = []
		for ch in linelist:
			try: 
				ch = int(ch)
			except:
				pass
			newline.append(ch)
			
		newline = newline[1:]
		cases.append(newline)
	#print cases
	
	casecount = 0
	for case in cases:
		casecount += 1
		type = "?"
		orangelist = []
		bluelist = []
		for ch in case:
			try: 
				int(ch)
			except ValueError:
				type = ch
			else:
				if type == "O":
					orangelist.append(ch)
				elif type == "B":
					bluelist.append(ch)
				else:
					print "Uh oh"
		#print "Case is ", case
		#print "Orange:", orangelist
		#print "Blue:", bluelist
		
		orange = Bot('Orange', orangelist)
		blue = Bot('Blue', bluelist)
		p = True
		ntype = "?"
		nnum = 0
		for x in range(1, 10100000):
			if p:
				try:
					ntype = case[0]
					nnum = case[1]
					case.pop(0)
					case.pop(0)
				except IndexError:
					print "Manager Done!"
					break
				p = False
			

			
			if ntype == 'O':
				r = orange.press()
				if r:
					p = True
			elif ntype == 'B':
				r = blue.press()
				if r:
					p = True
			else:
				print "Uh, oh #2"
			
			blue.tick()
			orange.tick()
			if blue.done() and orange.done():	
				win = 0
				if blue.tickcount > orange.tickcount:
					win = blue.tickcount
				elif orange.tickcount > blue.tickcount:
					win = orange.tickcount
				else:
					win = blue.tickcount
					print "Case #%d: %d" % (casecount, win)
				break
			
				
			
			
			
			
			
			
		
		
			