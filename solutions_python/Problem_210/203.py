import math
class event:
	def __init__(self, a, b):
		self.s = a
		self.e = b
	def __str__(self):
		return str(self.s) + 'and' + str(self.e)
def span(self, other):
	if self.s < other.s:
		e1 = self
		e2 = other
	else:
		e1 = other
		e2 = self
	span1 = e2.e - e1.s
	span2 = e1.e + 1440 - e2.s
	return min(span1, span2)
f = open("B-small-attempt1.in")
datainput = []
for l in f:
	datainput.append(l.strip())
totcase = int(datainput[0])
case = 1
p = 1
while case <= totcase:
	# print(str(p))
	ac = int(datainput[p].split(' ')[0])
	aj = int(datainput[p].split(' ')[1])
	# print("ac: {}, aj: {}".format(ac, aj))
	ac_list = []
	aj_list = []
	for i in range(ac):
		ac_list.append(event(int(datainput[p + 1 + i].split(' ')[0]), int(datainput[p + 1 + i].split(' ')[1])))
	for i in range(aj):
		aj_list.append(event(int(datainput[p + 1 + ac + i].split(' ')[0]), int(datainput[p + 1 + ac + i].split(' ')[1])))
	ex = 0
	if ac == 2:
		if span(ac_list[0], ac_list[1]) > 720:
			ex = 4
		else:
			ex = 2
	elif aj == 2:
		# print(aj_list[0], aj_list[1])
		# print(span(aj_list[0], aj_list[1]))
		if span(aj_list[0], aj_list[1]) > 720:
			ex = 4
		else:
			ex = 2
	else:
		ex = 2
	print("Case #{}: {}".format(case, ex))
	# print(span(event(900, 1260), event(180, 540)))
	# print(span(event(0, 1), event(720, 721)))
	p += 1 + ac + aj
	case += 1