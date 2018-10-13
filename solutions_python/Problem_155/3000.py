input_file = open('inputlarge.txt', 'r')
test_cases = int(input_file.readline())
output_data = []
for e in range(test_cases):
	l = input_file.readline()
	Smax = int(l.split(' ')[0])
	friends = 0
	audience = 0
	for i in range(Smax+1):
		quantity = int(l.split(' ')[1][i])
		shyness = i
		while audience < shyness:
			friends += 1
			audience += 1
		for x in range(quantity):
			audience += 1
	output_data.append((e+1, friends))

output_string = ""
for entry in output_data:
	output_string += "Case #"+str(entry[0])+": "+str(entry[1])
	output_string += "\n"
print output_string

output_file = open("output.txt", 'w')
output_file.write(output_string)
output_file.close()