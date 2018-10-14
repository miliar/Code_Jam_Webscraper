filename = "A-large.in"

# solve the standing ovation problem 
# based on the shyness information provided
def solve_standing_ovation(shyness):

	needs = 0
	total_ovation = 0

	# print shyness
	for i in range(len(shyness)):
		
		# print i, total_ovation
		if i > total_ovation:
			# not enough ovation to activate current ovation
			d = i - total_ovation
			needs += d
			total_ovation += d
		
		total_ovation += shyness[i]

	return needs

if __name__ == '__main__':

	fo = open(filename, "r+")

	T = fo.readline()
	# print T

	for i in range(int(T)):

		# parse
		L = fo.readline().strip()
		max_shy, shyness = L.split(" ")
		# max_shy = int(max_shy)
		shyness = map(lambda x: int(x), list(shyness))

		# solve
		S = solve_standing_ovation(shyness)

		# print
		print "Case #%d: %d" % (i + 1, S) 

