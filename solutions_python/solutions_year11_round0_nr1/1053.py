from sys import stdin

def parse_input(inFile):
	inFile.next() # skip first line

	for line in inFile:
		yield [(name, int(button)) for name, button in pairs(line.split()[1:])]

class Robot(object):
	def __init__(self, name, queue):
		self.button = 1
		self._target = None
		self.name = name
		self.queue = queue # shared
		self.done = False

	def tick(self):
		'''move towards the next button if not there. If already there, press if it is the first thing in the queue (i.e. other robot is done)'''
		# No more work
		if self.done:
			return

		# Not at the target yet
		t = self.target()

		if t is not None and t > self.button:
			self.button += 1
		elif t is not None and t < self.button:
			self.button -= 1

	def target(self):
		if self._target:
			return self._target

		for robot, button in self.queue:
			if robot == self.name:
				self._target = button
				return self._target

		self._target = None
		self.done = True
		return None

	def ready(self):
		'''At the target and target is the first item in the queue'''
		t = self.target()
		return t is not None and t == self.button and (self.name, t) == self.queue[0]

	def press(self):
		self.queue.pop(0)
		self._target = None

def pairs(li):
	"s -> (s0,s1), (s2,s3), (s4, s5), ..."
	return zip(li[::2], li[1::2])

for testCase, commandList in enumerate(parse_input(stdin)):
	orange = Robot('O', commandList)
	blue   = Robot('B', commandList)
	time   = 0
	while commandList:

		# Only one robot can push the button per turn. Both robots must check it's their turn _before_ either presses the button.
		readyRobot = filter(Robot.ready, (orange, blue))

		for robot in orange,blue:
			if robot in readyRobot:
				robot.press()
			else:
				robot.tick()

		time += 1

	print 'Case #%d: %d' % (testCase + 1, time)
