from sys import argv

script, input_file, output_file = argv

print "Input from %s \n Output into %s\n" % (input_file, output_file)

data = open(input_file,'r')
out = open(output_file,'w')

out.truncate()

num_of_cases = int(data.readline())

cases = []

for line in data:
	cases.append(line.strip('\n',).split()[1])

for i in range(num_of_cases):
	friends = 0
	standing = 0
	for Si in range(len(cases[i])):
		datum = cases[i]
		if Si == 0:
			standing += int(datum[Si])
			continue

		while Si > standing:
			friends +=1
			standing +=1
		
		standing += int(datum[Si])

	print "Case #%d: %d" % (i+1,friends)
	out.write("Case #%d: %d\n" % (i+1,friends))

data.close()
out.close()