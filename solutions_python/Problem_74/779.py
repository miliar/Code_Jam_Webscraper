import sys

def sign(v):
	if v > 0:
		return +1
	elif v < 0:
		return -1
	else:
		return 0

class Robot(object):
	def __init__(self, name):
		self.name = name
		self.button_no = 1
		self.task = []
		self.task_pos = 0
		self.other = None

	def move(self):
		if len(self.task) > 0 and self.task_pos < len(self.task):
			next_button = self.task[self.task_pos]
			if self.button_no != next_button:
				self.button_no += sign(next_button - self.button_no)
				#print self.name, 'move to button ', self.button_no
			else:
				#print self.name, 'stay at button ', self.button_no
				pass
		else:
			#print self.name, 'stay at button ', self.button_no
			pass

	def push_button(self):
		self.task_pos += 1
		


def other(r):
	if r == 0: return 1
	else: return 0

O = 'O'
B = 'B'

def process(fp):
	num_cases = int(fp.readline())
	for case in range(1,num_cases+1):
		#print '\n\n'
		task = []
		robots = {O:Robot(O), B:Robot(B)}
		robots[O].other = robots[B]
		robots[B].other = robots[O]
		line = fp.readline().replace('\n','')
		ls = line.split()
		num_buttons = int(ls[0])
		i = 1
		seq = 0
		for button in range(num_buttons):
			robot_name = ls[i]
			button_no = int(ls[i+1])
			robots[robot_name].task.append( button_no )

			task_item = (seq, robot_name, button_no)
			task.append(task_item)
			seq += 1
			i+=2

		#print task

		last_task_item = task[-1]
		time = 0
		finished = False
		for pos, task_item in enumerate(task):
			#print pos, task_item

			robot_name = task_item[1]
			button_no = task_item[2]

			robot = robots[robot_name]
			other = robot.other

			while robot.button_no != button_no:
				time += 1
				#print 'time ', time
				robot.button_no += sign(button_no - robot.button_no)
				#print robot.name, 'move to button ', robot.button_no

				other.move()


			time += 1
			#print 'time ', time
			#print robot.name, 'push button ', button_no
			robot.push_button()
			other.move()


		print 'Case #%d: %s' % (case, time)


if __name__ == '__main__':
	process(file(sys.argv[1]))
