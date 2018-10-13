class Robot(object):
	buttons = []
	pos = 1
	current = 0
	def __init__(self, buttons):
		self.buttons = [i[1] for i in buttons]
	def move(self):
		try:
			i=self.buttons[self.current]
			j=1 if self.pos < i else -1 if self.pos > i else 0
			self.pos += j
		except:
			j=0
		return j
	def try_press(self):
		try:
			if self.pos == self.buttons[self.current]:
				self.current+=1
				return True
			else:
				return False
		except:
			return False
		
class TestChamber(object):
	buttons = []
	orange, blue = None, None
	time = 0
	def __init__(self, buttons):
		self.buttons = buttons
		s=lambda x,y:filter(lambda z:z[0]==y,x)
		self.orange = Robot(s(buttons,'O'))
		self.blue = Robot(s(buttons,'B'))
	def move_robots(self):
		self.time+=1
		orange_move = self.orange.move()
		blue_move   = self.blue.move()
		orange_press, blue_press = False, False
		
		if not orange_move and self.next_button('O'):
			orange_press = self.orange.try_press()
		if not blue_move and not orange_press and self.next_button('B'):
			blue_press = self.blue.try_press()
		return self.orange.pos, orange_press, self.blue.pos, blue_press
	def get_time(self):
		return self.time
	def is_complete(self):
		return len(self.buttons) == self.orange.current + self.blue.current
	def next_button(self, robot_type):
		return robot_type == self.buttons[self.orange.current+self.blue.current][0]

def read_cases(cases):
	res, cs = [], cases.split('\n')
	n=int(cs[0])
	for case in cases.split('\n')[1:n+1]:
		l=case.split(" ")[1:]
		res.append([(l[i],int(l[i+1])) for i in range(0,len(l)-1,2)])
	return res

def test_robots(case):
	chamber = TestChamber(case)
	while not chamber.is_complete():
		chamber.move_robots()
	return chamber.time

def main():
	cases = read_cases(open('/Users/MiLaN/gcj1l.txt','r').read())
	out = open('/Users/MiLaN/gcj1lo.txt','w')
	for i in range(len(cases)):
		out.write("Case #%d: %d\n"%(i+1, test_robots(cases[i])))
	out.close()
		
main()