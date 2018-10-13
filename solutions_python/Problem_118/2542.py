import operator
import math

lines = [i.strip() for i in open("input.txt").readlines()]
f = open('outputsmall.txt','w')
num_cases = int(float(lines[0]));
cases=lines[1:num_cases+1]
c = 1
for case in cases:
    	min_max = case.split()
	min_num = min_max[0]
	max_num = min_max[1]
	max_range = int(math.floor(math.sqrt(int(float(min_max[1])))))
	min_range = int(math.ceil(math.sqrt(int(float(min_max[0])))))
	#print min_num, max_num
	#print min_range, max_range
	squares = list(x**2 for x in range(min_range,max_range+1))
	i = 0
	for square in squares:
		original = str(square)
		if original==original[::-1] and str(int(math.sqrt(float(square))))==str(int(math.sqrt(float(square))))[::-1]:
			i = i + 1
			#print original

	f.write("Case #" +str(c) +":"+" " + str(i) + '\n') 
	#print "Case #" +str(c) +":", str(i)
	c = c + 1


	