#!/usr/bin/env python

def main():
	inputf = open( "input", "r" )
	outputf = open( "output", "w" )
	data = inputf.read().split('\n')
	print data
        for idx, line in enumerate(data):
		if idx is 0:
			num = int(line)
		else:
			print '\n\nCase #'+str(idx)
			result = calculatecase( line )
			outputf.write('Case #'+str(idx)+': '+str(result)+'\n' )

def calculatecase(data):
	steps = 0
	inputs = data.split(' ')
	buttons = int(inputs[0])

	orangebot = CoolBot()
	bluebot = CoolBot()

	i = 0
	while i <= buttons:
		bot = inputs[ i*2 - 1 ]
		if bot is 'O':
			orangebot.presslist.append(int(inputs[ i*2 ]))
			print "orange has to move to "+ inputs[ i*2 ]
			print orangebot.presslist
		if bot is 'B':
			bluebot.presslist.append(int(inputs[ i*2 ]))
			print "blue has to move to "+ inputs[ i*2 ]
			print bluebot.presslist
		i += 1

	buttonspressed = 0
	while buttonspressed < buttons:
		print str(steps)+"th step"
		bot = inputs[ (buttonspressed+1)*2-1 ]
		incedsteps = False
		opress = orangebot.willpress()
		bpress = bluebot.willpress()
		oresult = False
		bresult = False

		if bot is 'O' and opress is True:
			oresult = orangebot.press()
			buttonspressed += 1
			bresult = bluebot.go()
			oresult = False
		if bot is 'B' and bpress is True:
			bresult = bluebot.press()
			buttonspressed += 1
			oresult = orangebot.go()
			bresult = False
		if bot is 'O' and opress is False or bot is 'B' and bpress is False:
			oresult = orangebot.go()
			bresult = bluebot.go()

		if oresult is not False:
			print "orange moves to "+ str(oresult)

		if bresult is not False:
			print "blue moves to "+ str(bresult)
		steps += 1

	return steps


def incsteps(steps,inced):
	if inced is True:
		return steps
	else:
		#steps += 1
		return steps

class CoolBot:
	pos = 1
	presslist = []
	topress = 0

	def __init__ (self):
		self.pos = 1
		self.presslist = []
		self.topress = 0

	def go (self):
		if len(self.presslist) is self.topress:
			return False
		print "Gotta press "+str(self.presslist[ self.topress ])+" and am at "+str(self.pos)
		if self.pos < self.presslist[ self.topress ]:
			self.pos += 1
			return self.pos
		elif self.pos > self.presslist[ self.topress ]:
			self.pos -= 1
			return self.pos
		else:
			return False
	def press(self):
		if self.pos is self.presslist[ self.topress ]:
			print "Pressed button at "+str(self.pos)
			self.topress += 1
			return True
	def willpress (self):
		if len(self.presslist) is self.topress:
			return False
		if self.pos is self.presslist[ self.topress ]:
			return True
		else:
			return False

if __name__ == '__main__':
                main()