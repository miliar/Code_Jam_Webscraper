#!/usr/bin/python

import sys

altitudes = []
bassin = []
current_letter = 'a'

# main function
# write code from here
def process(input, output):
	global altitudes
	global bassin
	global current_letter

	nb = int(input.readline().rstrip())

	for x_nb in range(1, nb+1):
		m_size = input.readline().rstrip()
		m_size = m_size.split()
		eabs = int(m_size[0])
		eord = int(m_size[1])

		altitudes = []
		bassin = []
		current_letter = 'a'


		def set_bassin_value(x, y):
			global altitudes
			global bassin
			global current_letter

			# we already have a value
			if bassin[x][y] != '':
				return bassin[x][y]

			# init cardinal access
			access_N = True
			access_W = True
			access_E = True
			access_S = True
			if x == 0:
				access_N = False
			if x == eabs-1:
				access_S = False
			if y == 0:
				access_W = False
			if y == eord-1:
				access_E = False

			access = [x, y]
			min_val = altitudes[x][y]
			if access_N and altitudes[x-1][y] < altitudes[x][y]:
				access[0] = x-1
				access[1] = y
				min_val = altitudes[x-1][y]
			if access_W and altitudes[x][y-1] < altitudes[x][y] \
				and altitudes[x][y-1] < min_val :
				access[0] = x
				access[1] = y-1
				min_val = altitudes[x][y-1]
			if access_E and altitudes[x][y+1] < altitudes[x][y] \
				and altitudes[x][y+1] < min_val :
				access[0] = x
				access[1] = y+1
				min_val = altitudes[x][y+1]
			if access_S and altitudes[x+1][y] < altitudes[x][y] \
				and altitudes[x+1][y] < min_val :
				access[0] = x+1
				access[1] = y
				min_val = altitudes[x+1][y]

			# final state
			if access[0] == x and access[1] == y:
				bassin[x][y] = current_letter
				current_letter = chr(ord(current_letter)+1)
				return bassin[x][y]

			bassin[x][y] = set_bassin_value(access[0], access[1])
			return bassin[x][y]

		# read altitudes
		for x in range(1, eabs+1):
			t = input.readline().rstrip().split()
			line = []
			for y in t:
				line.append(int(y))
			altitudes.append(line)

		# init bassin
		for x in range(eabs):
			bassin.append([])
			for y in range(eord):
				bassin[x].append('')

		# set bassin values
		for x in range(eabs):
			for y in range(eord):
				if bassin[x][y] == '':
					set_bassin_value(x, y)

		if ord(current_letter)-1 > ord('z'):
			raise 'lettre trop grand !'

		output.write('Case #%d:\n' %(x_nb))
		for x in range(eabs):
			output.write(' '.join(bassin[x]) + '\n')

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Need file as argument"
		sys.exit(1)

	input_file = sys.argv[1]

	# open the file
	input_handler = open(input_file, 'r')
	output_handler = open(input_file + '.out', 'w+')

	process(input_handler, output_handler)

	# close files
	input_handler.close()
	output_handler.close()
