class Ken:
	# Takes a list of blocks in sorted order
	# and stores them as Ken's blocks
	def __init__(self, blocks):
		self.blocks = blocks
		self.n_blocks = len(blocks)

	# Chooses a move based on the weight of naomi's block
	def choose_move(self, naomi):
		if self.blocks[self.n_blocks - 1] < naomi: # We can't beat naomi
			self.n_blocks -= 1
			return self.blocks.pop(0) # play the smallest block
		else:
			for block in self.blocks:
				if block > naomi: # Find the smallest block that is greater than naomi
					self.blocks.remove(block) # Remove this block
					self.n_blocks -= 1
					return block

class Simulator:
	# Takes two lists of blocks in sorted order
	# Naomi knows ken's blocks as well
	def __init__(self, naomi_blocks, ken_blocks, n_blocks):
		self.naomi_blocks = naomi_blocks
		self.ken_blocks = ken_blocks
		self.n_blocks = n_blocks

	# Returns the actual weight of the block chosen by naomi and its weight
	# as told to ken
	def choose_move_d(self):
		self.n_blocks -= 1
		# If we have a block less than all of Ken's blocks
		# Waste Ken's largest block
		if self.naomi_blocks[0] < self.ken_blocks[0]:
			actual = self.naomi_blocks.pop(0)
			ken = self.ken_blocks.pop()
			told =  ken - 0.00001 
			return (actual, told, ken)

		# We can knock this block
		else:
			actual = self.naomi_blocks.pop(0)
			told = self.ken_blocks[self.n_blocks] + 0.000001
			ken = self.ken_blocks.pop(0)
			return (actual, told, ken)

	# Just play the lowest block
	def choose_move(self):
		actual = told = self.naomi_blocks.pop(0) # Play the smallest block
		for block in self.ken_blocks:
			if block > actual:
				self.ken_blocks.remove(block)
				return (actual, told, block)
		return (actual, block, self.ken_blocks.pop(0))


file_input = open('DeceitfulWar_input')
file_output = open('DeceitfulWar_output', 'w')

input = file_input.readline
print = file_output.write

T = int(input())

for i in range(T):
	N = int(input())

	naomi_blocks = list(map(float, input().split()))
	ken_blocks = list(map(float, input().split()))

	naomi_blocks.sort()
	ken_blocks.sort()

	sim_d = Simulator(list(naomi_blocks), list(ken_blocks), N)
	sim_t = Simulator(list(naomi_blocks), list(ken_blocks), N)

	points = [0, 0]
	for _ in range(N):
		move_d = sim_d.choose_move_d()
		move_t = sim_t.choose_move()

		if(move_d[2] < move_d[0]):
			points[0] += 1
		if(move_t[2] < move_t[0]):
			points[1] += 1

	print('Case #' + str(i + 1) + ': ' + str(points[0]) + ' ' + str(points[1]) + '\n')


