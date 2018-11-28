import sys
import numpy
# K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.
# When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?
# 

FREE = 0
OCCUPIED = 1

class BathroomAssignement(object):
	def __init__(self, n_stalls, n_people):
		self.n_stalls = n_stalls
		self.n_people = n_people
		self.stalls_to_occupy = n_people
		self.default_occupation()
		self.free_stalls = {}
		#print self.occupation

	def default_occupation(self):
		occupation = [0 for i in range(self.n_stalls+2)]
		
		# right and leftmost are occupied by default
		occupation[0] = 1
		occupation[len(occupation)-1] = 1

		self.occupation = occupation
		#print occupation


	def assign_stall(self):
		free_stalls = {} 
		# to remove from dict: dict.pop(key)
		for stall, i in zip(self.occupation, range(len(self.occupation))):
			if stall is FREE:
				left_stalls = self.occupation[:i]
				right_stalls = self.occupation[(i+1):]

				# print "--"
				# print left_stalls
				# print right_stalls
				# print "-- "

				free_left = 0
				free_right = 0
				for l_stall in reversed(left_stalls):
					if l_stall is FREE:
						free_left += 1

					else:
						break
						#print " free left %i" %free_left

				for r_stall in right_stalls:
					if r_stall is FREE:
						free_right += 1 
						#print " free right %i" %free_right

					else: # because OBVIOSLY Jessica, you have to stop counting once you find an occupied stall
						break

				#if i not in free_stalls:
				free_stalls[i] = (free_left, free_right)

		#print free_stalls
		self.free_stalls = free_stalls
		best_stall, y, z = self.find_farthest_closest_neighbor()
		del self.free_stalls[best_stall]
		self.occupation[best_stall] = OCCUPIED
		self.stalls_to_occupy -= 1

		#if self.stalls_to_occupy == 0: # no more stalls to occupy
			#print "y = %i,  z = %i" %(y, z)
		return y, z

		#print self.occupation
				#else:

	def find_farthest_closest_neighbor(self):
		best_stall = -1
		best_value = -1

		which_best = []
		for stall in self.free_stalls:
			if min(self.free_stalls[stall][0], self.free_stalls[stall][1]) >= best_value:
				best_stall = stall
				best_value = min(self.free_stalls[stall][0], self.free_stalls[stall][1])
				#print min(self.free_stalls[stall][0], self.free_stalls[stall][1])
				#print " stall" + str(stall)
				#which_best.append(stall) # need to verify when more than one


		best_value2 = -1
		for stall in self.free_stalls:
			if min(self.free_stalls[stall][0], self.free_stalls[stall][1]) == best_value:
				#print "jjj"
				if max(self.free_stalls[stall][0], self.free_stalls[stall][1]) >= best_value2:
					#print "ssskj"
					#best_value2 = max(self.free_stalls[stall][0], self.free_stalls[stall][1])
					if max(self.free_stalls[stall][0], self.free_stalls[stall][1]) == best_value2:
						pass
					else: # so we get the leftmost???
						best_value2 = max(self.free_stalls[stall][0], self.free_stalls[stall][1])
						best_stall = stall
						#print "sjs"
						#print best_stall

		# print "best stall: %i" %(best_stall)
		# print self.free_stalls[best_stall]
		y = max(self.free_stalls[best_stall][0], self.free_stalls[best_stall][1]) # y
		z = min(self.free_stalls[best_stall][0], self.free_stalls[best_stall][1]) # z

		# del self.free_stalls[best_stall]
		# self.occupation[best_stall] = OCCUPIED
		return best_stall, y, z


def parse_input_file(fn):
	with open(fn, "r")  as f:
		lines = f.readlines()

	nbr_inputs = int(lines[0])
	lines = lines[1:]
	inputs = []
	for l in lines:
		n_stalls, n_people = l.split(" ")
		n_stalls = int(n_stalls)
		n_people = int(n_people)

		bath_assg = BathroomAssignement(n_stalls, n_people)
		inputs.append(bath_assg)
		#inputs.append( (n_stalls, n_people) )

	return inputs


def assign_stall(n_stalls, occupation):
	pass

def main():
	if len(sys.argv) == 2:
		#print sys.argv[1]
		inputs = parse_input_file(sys.argv[1])

		for inp, i in zip(inputs, range(len(inputs))):
			#print "***"
			while inp.stalls_to_occupy != 0:
				y, z = inp.assign_stall()

			print "Case #%i: %i %i" %(i+1, y, z)
			#print inp.occupation

	else:
		print "something is not right. Have you forgetten the input file?"

if __name__ == "__main__":
	main()