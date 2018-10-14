class robot:
	def __init__(self, name,btn_list):
		self.can_start = False
		self.cur_loc = 1
		self.btn_list = []
		self.name = name
		for i in btn_list:
			if i['hall'] == self.name:
				self.btn_list.append(i['num'])


	def move(self):
		if len(self.btn_list) == 0:
			return False
		if self.btn_list[0] < self.cur_loc:
			step = -1
		elif self.btn_list[0] > self.cur_loc:
			step = 1
		else:
			return False
		self.cur_loc += step
		return True

	def push(self, btn_to_push):
		if self.can_start == False:
			return False
		if len(self.btn_list) == 0:
			return False
		if btn_to_push['hall'] == self.name and self.cur_loc == self.btn_list[0]:
			del self.btn_list[0]
			return True
		else:
			return False

def process():
	time = 0
	global g_btn_list
	O = robot("O", g_btn_list)
	B = robot("B", g_btn_list)
	if g_btn_list[0]['hall'] == "B":
		B.can_start = True
	else:
		O.can_start = True
	while len(g_btn_list) != 0:
		time += 1
		b_can_push = True
		if O.move() == False:
			if O.push(g_btn_list[0]) == True:
				del g_btn_list[0]
				B.can_start = True
				b_can_push = False
		if B.move() == False:
			if b_can_push == False:
				continue
			if B.push(g_btn_list[0]) == True:
				del g_btn_list[0]
				O.can_start = True

	return time

g_btn_list = []
input = open(".\A-large.in", "r")
cases = int(input.readline())
for i in range(1,cases+1):
	tokens = input.readline().split()
	n = int(tokens[0])
	del tokens[0]
	for j in range(n):
		btn = {}
		btn['hall'] = tokens[0]
		del tokens[0]
		btn['num'] = int(tokens[0])
		del tokens[0]
		g_btn_list.append(btn)
	print 'Case #%d: %d' % (i,process())
	g_btn_list = []

input.close()
