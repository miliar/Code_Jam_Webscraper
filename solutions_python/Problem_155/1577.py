input_file = "A-large.in"
output_file = "output.txt"

data = open(input_file, 'r')
output = open(output_file, 'w')


test_case = (int)(data.readline())

for i in range(test_case):
	line = data.readline().split()
	shy_max = line[0]
	person_info = line[1]
	standing = 0
	needed = 0
	for j in range(len(person_info)):
		if( (j) > standing ):
			needed += j - standing
			standing += j - standing
		standing += int(person_info[j])
	
	output.write("Case #%d: %d\n" %(i+1, needed))

output.close()
