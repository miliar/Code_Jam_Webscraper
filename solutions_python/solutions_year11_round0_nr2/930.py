import threading, time, sys, re
inData = open(sys.argv[1]).read().strip()
#inData = """5
#0 0 2 EA
#1 QRI 0 4 RRQR
#1 QFT 1 QF 7 FAQFDFQ
#1 EEZ 1 QE 7 QEEEERA
#0 1 QW 2 QW"""
class Awesome(threading.Thread):
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i
		self.done = False
		self.st = time.time()
	def run(self):
		data = self.i.split(" ")
		combine = {}
		explode = {}
		combineCnt = 0
		explodeCnt = 0
		step = 0
		for k,v in enumerate(data):
			if k == 0 and step == 0:
				combineCnt = int(v)
				step = 1
				if combineCnt <= 0:
					step = 2
				continue
			elif combineCnt > 0 and step == 1:
				if v[0] not in combine:
					combine[v[0]] = {}
				combine[v[0]][v[1]] = v[2]
				if v[1] not in combine:
					combine[v[1]] = {}
				combine[v[1]][v[0]] = v[2]
				combineCnt -= 1
				if combineCnt <= 0:
					step = 2
					continue
			elif step == 2:
				explodeCnt = int(v)
				step = 3
				if explodeCnt <= 0:
					step = 4
				continue
			elif step == 3 and explodeCnt > 0:
				if v[0] not in explode:
					explode[v[0]] = []
				explode[v[0]].append(v[1])
				if v[1] not in explode:
					explode[v[1]] = []
				explode[v[1]].append(v[0])
				explodeCnt -= 1
				if explodeCnt <= 0:
					step = 4
					continue
			elif step == 4:
				if re.match("^([0-9]+)$", v):
					step = 5
			elif step == 5:
				stack = []
				stackturn = []
				for a, x in enumerate(v):
					stack = stack[:len(stack)]
					if len(stack) > 0:
						if stack[-1] in combine and x in combine[stack[-1]]:
							stack.append(combine[stack[-1]][x])
							del stack[-2]
						elif x in explode:
							for kaboom in explode[x]:
								if kaboom in stack:
									stack = []
									stackturn.append("BOOM appending "+x+" to "+kaboom)
									break
							if len(stack) > 0:
								stack.append(x)
						else:
							stack.append(x)
					else:
						stack.append(x)
					stackturn.append([a,x,stack])
				step = 6
			else:
				break
		self.explode = explode
		self.combine = combine
		self.stackturn = stackturn
		self.out = `stack`.replace("'", "")
		self.done = time.time()

th = []
for i in inData.split("\n")[1:]:
	th.append(Awesome(i))
	th[-1].start()
for k,i in enumerate(th):
	while True:
		if i.done:
			print "Case #%s: %s" % (k+1, i.out)
			#if k == 2:
			#	print i.stackturn
			break
for i in th:
	sys.stderr.write("%s finished in %s\n"%(i.name, i.done - i.st))
