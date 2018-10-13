import fileinput

class MagicanTrick(object):
	def __init__(self, case):
		self.case = case
		self.answer = None
		self.answer2 = None
		self.card_square = set([])
		self.card_square2 = set([])

	def set_card_square_row(self, square_number, line):
		for number in line[:-1].split():
			if square_number == 1:
				self.card_square.add(int(number))
			else:
				self.card_square2.add(int(number))

	def print_result(self):
		result_set = self.card_square & self.card_square2
		if len(result_set) == 1:
			print "Case #{}: {}".format(self.case, result_set.pop())
		elif len(result_set) >= 2:
			print "Case #{}: Bad magician!".format(self.case)
		elif len(result_set) == 0:
			print "Case #{}: Volunteer cheated!".format(self.case)






case = 1
mt = MagicanTrick(case)
for index, line in enumerate(fileinput.input()):
	if index == 0: continue
	own_index = (index - 1) % 10
	#print line[:-1] + '#' + str(own_index)
	if own_index == 0:
		mt.answer = int(line[:-1])
		#print "ANSWER1", mt.answer

	elif own_index == mt.answer:
		mt.set_card_square_row(1, line)

	elif own_index == 5:
		mt.answer2 = int(line[:-1]) + 5
		#print "ANSWER2", mt.answer2

	elif own_index == mt.answer2:
		mt.set_card_square_row(2, line)
		mt.print_result()
		case = case + 1
		mt = MagicanTrick(case)
