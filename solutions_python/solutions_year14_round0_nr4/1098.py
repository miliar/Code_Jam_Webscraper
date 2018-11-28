#!/usr/bin/env python
#from pprint import pprint

class DeceitfulWar():
	def __init__(self, block_count, naomi, ken):
		self.block_count = block_count
		self.naomi = naomi
		self.ken = ken
		self.straight_win = True
		self.naomi_fake_pt = 0
		self.naomi_real_pt = 0
		self.naomi_left_real_pt = 0
		self.epsilon = 0.000001

		self.calculate_real_pt()

	def calculate_real_pt(self):
		ken_pt = 0
		ken_i = 0
		naomi_i = 0

		ken_blocks = [x for x in self.ken]

		while (naomi_i < self.block_count):
			while (ken_i < len(ken_blocks)):
				if (ken_blocks[ken_i] > self.naomi[naomi_i]):
					ken_pt += 1
					ken_blocks.pop(ken_i)
					ken_i = 0
					break
				else:
					ken_i += 1
			naomi_i += 1
		self.naomi_real_pt = self.block_count - ken_pt

	def get_real_pt(self):
		return self.naomi_real_pt

	def get_fake_pt(self):
		return self.naomi_fake_pt

	def play(self):
		while(self.block_count > 0):
			self.straight_win_fun()

			if (self.straight_win):
				self.naomi_fake_pt += self.naomi_left_real_pt
				break
			else:
				self.naomi.pop(0)
				self.ken.pop()
				self.block_count -= 1

	def straight_win_fun(self):
		# pprint(naomi)
		# print "---------------"
		# pprint(ken)
		# print "==============="
		self.straight_win = True
		self.naomi_left_real_pt = 0
		for i in range(self.block_count):
			if (self.naomi[i] > self.ken[i]):
				self.naomi_left_real_pt += 1
			else:
				self.straight_win = False
				break

input = "D-large.in"
#input = "D-small-attempt0.in"
with open(input) as myfile:
	lines = myfile.read().splitlines();

#myfile = open('D-small-attempt0.out','w')
myfile = open('D-large.out','w')

count = int(lines[0])
index = 1

for i in range(count):
	#print "case #", i + 1
	block_count = int(lines[index])

	naomi = lines[index + 1].split(" ")
	naomi.sort()
	ken = lines[index + 2].split(" ")
	ken.sort()

	dw = DeceitfulWar(block_count, naomi, ken)
	dw.play()
	naomi_fake_pt = dw.get_fake_pt()
	naomi_real_pt = dw.get_real_pt()

	index += 3

	myfile.write("Case #{}: {} {}\n".format(i + 1, naomi_fake_pt, naomi_real_pt))

myfile.close()