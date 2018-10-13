from cjlib.input import *
from cjlib.runner import TaskRunner, DummyRunner, MPQRunner
import logging

logging.basicConfig(level=logging.DEBUG)

class Game:
	size = 0
	others = []
	def absorb(self, obj):
		self.others.remove(obj)
		self.absorb_new(obj, True)
		logging.debug("Absorbed %d. My size %d", obj, self.size)
	def absorb_new(self, obj, call_from_absorb=False):
		if obj >= self.size:
			raise Exception, "Fucker"
		self.size += obj
		if not call_from_absorb:
			logging.debug("Created and absorbed %d. My size %d", obj, self.size)

def process(case, mySize=None, otherMotes=[]):
	m = Game()
	m.size = case[0][0]
	m.others = case[1]
	turnCnt = 0
	ops = 0
	while len(m.others) > 0:
		smallers = [x for x in m.others if x < m.size]
		turnCnt += 1
		if len(smallers) > 0:
			m.absorb(max(smallers))
		else:
			# we need to add or remove.
			wantTo = [x for x in m.others if x < m.size + (m.size - 1)]
			if len(wantTo) == 0:
				opsIfRemove = len(m.others)
				opsIfAdd = -1
				if m.size > 1:
					opsIfAdd = 0
					targetSize = min(m.others)
					size = m.size
					while size <= targetSize:
						size += size-1
						opsIfAdd += 1
				if opsIfAdd < opsIfRemove and opsIfAdd != -1:
					# add and continue playing
					logging.debug("Absorbed stuff. My size %d", m.size)
					m.size = size
					ops += opsIfAdd
				else:
					# use remove strategy
					ops += opsIfRemove
					break
			else:
				m.absorb_new(m.size-1)
				ops += 1
				m.absorb(max(wantTo))
	return ops

get("""4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1
10
9 20 25 100
10
9 13 19""")

r = TaskRunner(process, DummyRunner)

while neof():
	l = [int(x) for x in line().split(" ")]
	l2 = [int(x) for x in line().split(" ")]
	r.add([l, l2])

r.run(True)