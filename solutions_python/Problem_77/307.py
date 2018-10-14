import os

def read_vector(s, vector_length):
	vector = []
	index_start = 0
	for _ in xrange(0, vector_length-1): 
		index_end = s.find(" ", index_start)
		vector.append(int(s[index_start:index_end]))
		index_start = index_end + 1
	vector.append(int(s[index_start:]))
	return vector

filepath = "/home/mike/Downloads/"
filename = "D-large"

f_in = open(os.path.join(filepath, filename+".in"), "rb")
f_out = open(os.path.join(filepath, filename+".out"), "wb")
num_test_cases = int(f_in.readline())

for test_case in xrange(1, num_test_cases+1):
#for test_case in xrange(1, 5):
	N = int(f_in.readline())
	V = read_vector(f_in.readline(), N)
	Vs = sorted(V)
	
	proper = 0
	for i in xrange(0, len(V)):
		if (V[i] == Vs[i]): proper += 1
		 
	#print N, V, Vs, len(V)-proper
				
	output = "Case #%d: %5f" % (test_case, len(V)-proper)
	print output
	f_out.write(output+"\n")

f_out.close()