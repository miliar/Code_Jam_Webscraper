import re

input_file = open('A-large.in', 'r+')

input = input_file.readlines()


(L, D, N) = input[0].split(" ");
(L, D, N) = (int(L), int(D), int(N))

#print L, D, N


line = input[6]
result_matrix = []
for i in range(0,N):
	result_matrix.append(0);
        line = input[1 + D + i]
	line = line.replace("(","[").replace(")","]")
	#print line
	for j in range(0, D):
		word = input[1 + j]
		#print word
		if re.match(line, word):
			#print "punto"
			result_matrix[i] = result_matrix[i] + 1


x = 0;
for i in result_matrix:
	x = x + 1
	print "Case #%d: %d" % (x, i) 
