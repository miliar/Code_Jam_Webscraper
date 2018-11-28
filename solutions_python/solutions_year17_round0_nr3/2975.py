input_file = open('C-small-1-attempt2.in','r')
num_inputs = int(input_file.readline())

output_file = open('output.out', 'a')

class Stall:
	occupied = False
	l_s = None
	r_s = None
	
	def __init__(self, occupied):
		if occupied:
			self.occupied = True
		else:
			self.occupied = False
	def __str__(self):
		return 'O00' if self.occupied else '___ ('+str(self.l_s)+','+str(self.r_s) +')'
	def __repr__(self):
		return 'O00' if self.occupied else '___ ('+str(self.l_s)+','+str(self.r_s) +')'

	def update_ls(self, ls):
		self.l_s = ls
	def update_rs(self, rs):
		self.r_s = rs

	def max_ls_rs(self):
		if (self.occupied):
			return -9999999
		return max(self.l_s, self.r_s)
	def min_ls_rs(self):
		if (self.occupied):
			return 99999999
		return min(self.l_s, self.r_s)


class Stalls:
	num_stalls = 0
	num_to_place = 0
	num_placed = 0
	stalls = []
	def __init__(self, num_stalls, num_people, case):
		# if num_people >  num_stalls / 2:
		# 	output_string = 'Case #' + str(case) + ': 0 0'
		# else:
		self.num_stalls = num_stalls + 2
		self.num_to_place = num_people
		self.stalls = [Stall(True)] + [Stall(False) for x in range(num_stalls)] + [Stall(True)]
		self.update_ls_rs()
		output = None
		for person in range(num_people):
			output = self.insert_person()
		output_string = 'Case #' + str(case) + ': ' + str(output[0]) + ' ' + str(output[1])
		print(output_string)
		output_file.write(output_string+'\n')

	def update_ls_rs(self):
		for x in range(self.num_stalls):
			self.stalls[x].update_ls(self.get_ls(x))
			self.stalls[x].update_rs(self.get_rs(x))

	def get_ls(self, index):
		if self.stalls[index].occupied == True:
			return None
		for x in range(-1 + index, -1, -1):
			if self.stalls[x].occupied == True:
				return index - x - 1

	def get_rs(self, index):
		if self.stalls[index].occupied == True:
			return None
		for x in range(index, self.num_stalls):
			if self.stalls[x].occupied == True:
				return x - index - 1

	def __str__(self):
		return ''.join(str(self.stalls))

	def get_max_min_ls_rs_indices(self):
		m = -99999999999999
		indices = []
		for x in range(self.num_stalls):
			if (self.stalls[x].occupied == True):
				continue
			else:
				if (self.stalls[x].min_ls_rs() > m):
					m = self.stalls[x].min_ls_rs()

		for x in range(self.num_stalls):
			if (self.stalls[x].occupied == True):
				continue
			elif (self.stalls[x].min_ls_rs() == m):
				indices.append(x)
		return indices

	def get_max_max_ls_rs_indices(self, check_indices):
		m = -99999999999999
		indices = []
		for x in check_indices:
			if (self.stalls[x].occupied == True):
				continue
			if (self.stalls[x].max_ls_rs() > m):
				m = self.stalls[x].max_ls_rs()

		for x in check_indices:
			if (self.stalls[x].occupied == True):
				continue
			if (self.stalls[x].max_ls_rs() == m):
				indices.append(x)
		return indices

	# def get_max_mins(self, mins):


	def insert_person(self):
		y = -1
		z = -1
		self.update_ls_rs()
		mins = self.get_max_min_ls_rs_indices()
		index_to_occupy = -1
		if len(mins) == 1:
			index_to_occupy = mins[0]
		else:
			maxs = self.get_max_max_ls_rs_indices(mins)
			index_to_occupy = maxs[0]
		output = self.stalls[index_to_occupy].max_ls_rs(), self.stalls[index_to_occupy].min_ls_rs()
		self.stalls[index_to_occupy].occupied = True
		self.stalls[index_to_occupy].update_ls(None)
		self.stalls[index_to_occupy].update_rs(None)
		return output

for x in range(num_inputs):
	i = input_file.readline().strip().split(' ')
	num_stalls = int(i[0])
	num_people = int(i[1])
	stalls = Stalls(num_stalls, num_people, x+1)
# output_file.close()