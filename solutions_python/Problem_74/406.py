class Bot:
	def __init__(self, color, order):
		self.color = color
		self.order = order
		self.position = 1
		self.lastAction = 0

	def step(self, time, step):
		""" Calculate the finishing time of the operation """
		s = self.order[step]
		# time to walk
		walk = abs(s[1] - self.position)
		
		# how long was I doing nothing
		nothing = time - self.lastAction
		 
		if walk > nothing: # if I am longer walking than doing nothing
			nextTime = time + walk - nothing + 1
		else: # Ill be on my spot, and can push the button in 1 sec
			nextTime = time + 1

		# update stats
		self.lastAction = nextTime
		self.position = s[1]

		return nextTime


f = open("A-large.in")
out = open("A-large.out", "w")


lines = f.readlines()
cases = int(lines.pop(0))


for case in range(cases):
	c = lines.pop(0)
	# create the commands
	commands = c.split(' ')
	steps = int(commands.pop(0))
	order = []
	for s in range(steps):
		order.append((commands.pop(0), int(commands.pop(0))))

	# create the bots
	bots = {"O":'', "B":''}

	for b in bots:
		bots[b] = Bot(b, order)

	time = 0
	for s in range(steps):
		time = bots[order[s][0]].step(time, s)
	
	out.write("Case #%d: %d\n" %(case + 1, time))

f.close()
out.close()
