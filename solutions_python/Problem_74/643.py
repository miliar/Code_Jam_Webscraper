import sys, itertools
filename = sys.argv[1]
f = open(filename)
o = open(filename + ".out", "wt")

def grouper(n, iterable, fillvalue=None):
	"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return itertools.izip_longest(fillvalue=fillvalue, *args)
	
class Robot():
	def __init__(self, col):
		self.col = col
		self.ptr = -1
		self.dest = -1
		self.pos = 1
		self.cur_btn = -1
		self.dir = 0
		
	def at_dest(self):
		a = self.dest
		b = self.pos
		#print "**", a, b, type(a), type(b), a == b
		return self.dest == self.pos
	
	def is_finished(self):
		return self.dest == None
		
def get_next_dest(cmd_list, robot):
	#print cmd_list
	for i in range(robot.ptr + 1, len(cmd_list)):
		cmd = cmd_list[i]
		if cmd[0] == robot.col:
			robot.ptr = i
			robot.cur_btn = i
			robot.dest = cmd[1]
			robot.dir = 1 if robot.dest > robot.pos else -1
			return
	robot.at_end = True
	robot.dest = None

num_tests = int(f.readline())
for t in range(1, num_tests+1):
	d = f.readline().split()
	n = int(d[0])
	d = d[1:]
	cmd = [(c[0], int(c[1])) for c in grouper(2, d)]

	robots = [Robot('O'), Robot('B')]
	
	buttons_pressed = [False for i in range(0, len(cmd))]
	cur_btn = 0
	
	get_next_dest(cmd, robots[0])
	get_next_dest(cmd, robots[1])
	
	time = 1
	while not (robots[0].is_finished() and robots[1].is_finished()):
		#print "Time: ", time, ": "
		pushed = -1
		for r in robots:
			#print "col: ", r.col, "pos: ", r.pos, "dest: ", r.dest,
			if not r.is_finished():
				#print "not finished", 
				if r.at_dest():
					#print "at dest", 
					ok_to_press = cur_btn == r.cur_btn or all([b for b in buttons_pressed[:r.cur_btn]])
					if ok_to_press:
						#print "Push button", r.pos
						pushed = r.cur_btn
						#print r.ptr, cmd
						get_next_dest(cmd, r)
						#print "Next", r.dest
						r.dir = 1 if r.dest > r.pos else -1
						#cmd = cmd[1:]
					else:
						pass
						#print "Stay at button", r.pos
				else:
					r.pos = r.pos + r.dir
					#print "Move to button", r.pos


		if pushed != -1:
			buttons_pressed[pushed] = True
			pushed = -1
		time += 1
	o.write("Case #%d: %d\n" % (t, time-1))
o.close()