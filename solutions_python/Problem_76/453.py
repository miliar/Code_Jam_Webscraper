import os
import itertools

def read_vector(s, vector_length):
	vector = []
	index_start = 0
	for _ in xrange(0, vector_length-1): 
		index_end = s.find(" ", index_start)
		vector.append(int(s[index_start:index_end]))
		index_start = index_end + 1
	vector.append(int(s[index_start:]))
	return vector

def add(list):
	value = 0
	for item in list: 
		value += item
	return value

def xor(list):
	value = 0
	for item in list: 
		value ^= item
	return value


filepath = "/home/mike/Downloads/"
filename = "C-small-attempt1"

f_in = open(os.path.join(filepath, filename+".in"), "rb")
f_out = open(os.path.join(filepath, filename+".out"), "wb")
num_test_cases = int(f_in.readline())

for test_case in xrange(1, num_test_cases+1):
#for test_case in xrange(1, 5):
	N = int(f_in.readline())
	C = read_vector(f_in.readline(), N)

	for i in xrange(1, N):
		indices = range(0, N)
		combinations = list(itertools.combinations(indices, i))
		patrick = []
		max_value_sean = None
		
		sean = []
		#print combinations
		for combination in combinations:
			new_sean = []
			new_patrick = []
			for index in indices:
				if (index in combination):
					new_sean.append(C[index])
				else:
					new_patrick.append(C[index])
					
			sean.append(new_sean)
			patrick.append(new_patrick)
						
		#print sean, patrick

		for j in xrange(0, len(sean)):
			#print "xor:", xor(sean[j]), xor(patrick[j])
			if (xor(sean[j]) == xor(patrick[j])) and ((max_value_sean == None) or (add(sean[j]) > max_value_sean)):
				max_value_sean = add(sean[j])
				
	output = "Case #%d: %s" % (test_case, (max_value_sean, "NO")[max_value_sean == None])
	#print output
	f_out.write(output+"\n")

f_out.close() 