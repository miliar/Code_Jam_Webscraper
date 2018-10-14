import threading, time, sys, re
inData = open('a-small.in').read().strip()
#inData = """3
#4 O 2 B 1 B 2 O 4
#3 O 5 O 8 B 100
#2 B 2 B 1"""
class Awesome(threading.Thread):
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i
		self.done = False
		self.st = time.time()
		self.orange = 1
		self.blue = 1
		self.turn = 0
		self.turnData = []
	def run(self):
		# parse the format
		x = re.findall("([OB] [0-9]+)+", self.i)
		x = map(lambda x: x.split(" "), x)
		blueGoal = None
		orangeGoal = None
		blueInd = None
		orangeInd = None
		procInd = []
		while self.turn <= 2000:
			turnData = ["", "", []]
			if not blueGoal:
				for k,i in enumerate(x):
					if k in procInd: continue
					if i[0] == "B":
						blueGoal = int(i[1])
						blueInd = k
						procInd.append(k)
						break
			if not orangeGoal:
				for k,i in enumerate(x):
					if k in procInd: continue
					if i[0] == "O":
						orangeGoal = int(i[1])
						orangeInd = k
						procInd.append(k)
						break
			if blueGoal == None and orangeGoal == None:
				break
			turnData[2] = [[blueGoal, blueInd], [orangeGoal, orangeInd]]
			self.turn += 1
			bluePress = False
			# make a step or skip
			if blueGoal:
				if blueGoal != self.blue:
					if blueGoal - self.blue < 0:
						self.blue -= 1
						turnData[0] = "B: Walk back 1 tile - "+str(self.blue)
					else:
						self.blue += 1
						turnData[0] = "B: Walk ahead 1 tile - "+str(self.blue)
				elif blueGoal == self.blue:
					if  blueInd < orangeInd or orangeInd == None:
						# press!
						blueGoal = None
						blueInd = None
						bluePress = True
						turnData[0] = "B: Press "+str(self.blue)
					else:
						turnData[0] = "B: Orange is blocking - "+str(self.blue)
			else:
				turnData[0] = "B: We're done here"
			if orangeGoal:
				if orangeGoal != self.orange:
					if orangeGoal - self.orange < 0:
						self.orange -= 1
						turnData[1] = "O: Walk back 1 tile - "+str(self.orange)
					else:
						self.orange += 1
						turnData[1] = "O: Walk ahead 1 tile - "+str(self.orange)
				elif orangeGoal == self.orange:
					if not bluePress and (orangeInd < blueInd or blueInd == None):
						# press!
						orangeGoal = None
						orangeInd = None
						turnData[1] = "O: Press "+str(self.orange)
					else:
						turnData[1] = "O: Blue is blocking - "+str(self.orange)
			else:
				turnData[1] = "O: We're done here"
			self.turnData.append(turnData)
		self.done = time.time()

th = []
for i in inData.split("\n")[1:]:
	th.append(Awesome(i))
	th[-1].start()
for k,i in enumerate(th):
	while True:
		if i.done:
			print "Case #%s: %s" % (k+1, i.turn)
			#if k+1 == 5:
			#	print i.turnData
			break
for i in th:
	sys.stderr.write("%s finished in %s\n"%(i.name, i.done - i.st))
