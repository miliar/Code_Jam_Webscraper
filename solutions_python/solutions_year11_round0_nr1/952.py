def solve(what, pos, idle):
	if not what:
		return 0
	who = what[0].who
	time = abs(pos[who]-what[0].where)+1-idle[who]
	if time < 1: time = 1
	pos[who] = what[0].where
	idle[who] = 0
	idle[1-who] = idle[1-who]+time
	return time + solve(what[1:], pos, idle)

cases = input()
		
class elem:
	def __init__(self, where, who):
		self.where = where
		self.who = who
	def __repr__(self):
		return "elem(where=%d,who=%d)"%(self.where, self.who)
		
for j in range(cases):
	e = raw_input().split(' ')
	n = int(e[0])
	lista = []

	for i in range(len(e)/2):
		cosa = elem(who=0 if e[1+i*2] == 'O' else 1, where=int(e[2+i*2]))
		lista += [cosa]
	print "Case #%d: %d"%(j + 1, solve(lista, [1, 1], [0, 0]))

