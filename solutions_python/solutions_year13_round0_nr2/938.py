#!/usr/bin/python

class Lawnmower:

	def __init__(self,input_lines):
		#print input_lines
		self.grass = [ [ int(i) for i in line.split() ] for line in input_lines ]
		#print self.grass
		value_list = []
		for i in xrange(len(self.grass)):
			for j in xrange(len(self.grass[0])):
				value_list.append(self.grass[i][j])
		#print value_list
		self.sorted_value_list = list(set(value_list))
		self.sorted_value_list.sort()
		#print self.sorted_value_list

	
	def solve(self):
		for h in self.sorted_value_list:
			#print "height: " + str(h)
			for i in xrange(len(self.grass)):
				#print "column: " + str(i)
				for j in xrange(len(self.grass[i])):
					#print "line: " + str(j)
					if h == self.grass[i][j]:
						line_works = True
						column_works = True
						for x in xrange(len(self.grass)):
							#print self.grass
							#print point_works
							#print x
							#print h
							if self.grass[x][j] > h:
								line_works = False
								break

						#print point_works

						for x in xrange(len(self.grass[i])):
							#print self.grass
							#print x
							#print h
							if self.grass[i][x] > h:
								column_works = False
								break

						#print point_works

						if (not line_works) and (not column_works):
							return False
		return True



import sys
input_lines = open(sys.argv[1], "rt").readlines()
stripped_input_lines = [line.strip() for line in input_lines]
num_tests = int(input_lines[0])
#print num_tests
curr_test = 1
curr_line = 1

while(curr_test<=num_tests):
	num_lines = int(stripped_input_lines[curr_line].split()[0])
	lawnmower = Lawnmower(stripped_input_lines[curr_line+1:curr_line+1+num_lines])
	result =  lawnmower.solve()
	if result:
		print "Case #"+str(curr_test)+": YES"
	else:
		print "Case #"+str(curr_test)+": NO"
	curr_test+=1
	curr_line += num_lines + 1
