filename = "A-large.in"

data = open(filename, 'r').readlines()
output_file = open("output.txt", 'w')

test_cases = int(data[0])

for i in range(1, test_cases + 1):
	s_max = int(data[i].split()[0])
	people = [None] * (s_max + 1)
	clappers = 0
	friends = 0
	for k in range(s_max + 1):
		people[k] = int(data[i].split()[1][k])
		if clappers >= k:
			clappers += people[k]
		else:
			while clappers < k:
				friends += 1
				clappers += 1
			clappers += people[k]
	output = "Case #%s: %s\n" % (i, friends)
	output_file.write(output)
			
				
		
		
		
	
		
		