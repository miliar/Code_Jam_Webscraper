def check_case(data):
	data = data.split()
	max_shy = int(data[0])
	a = []
	for i in range(0, max_shy + 1):
		a.append(int(data[1][i]))
	s = a[0]
	i = 1
	result = 0
	
	while (i < max_shy + 1) :

		if (s < i and a[i] != 0) :

			result += i - s
			s += i - s
		s += a[i]
		i += 1
	return result
		
		
		

f = open("/home/jancio/Downloads/A-large.in")
num_tests = int(f.readline())
out = open("out.out", "w")
for i in range(0, num_tests):
	out.write( "Case #" + str(i+1) + ": " + str(check_case(f.readline()))+"\n")
	
f.close()
out.close()
