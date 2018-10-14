import sys

# get command line arguments
if len(sys.argv) != 2:
        print 'Usage: '+sys.argv[0]+' input'
        sys.exit(-1)

# read input file
f = open(sys.argv[1],'r')
lines = f.readlines()
num_test_case = int(lines[0])

for i in range(num_test_case):
	output = 0
	data = lines[i+1].split(' ')
	num_dancer = int(data[0])
	num_suprise = int(data[1])
	p = int(data[2])
	for j in range(num_dancer):
		score = int(data[j+3])
		if score%3 == 0:
			if p <= score/3:
				output += 1
			elif p - score/3 == 1 and score/3 > 0:
				if num_suprise > 0:
					num_suprise -= 1
					output += 1
		elif score%3 == 1:
			if p <= (score/3)+1:
				output += 1
		elif score%3 == 2:
			if p <= (score/3)+1:
                                output += 1
			elif p - score/3 == 2:
				if num_suprise > 0:
                                        num_suprise -= 1
                                        output += 1
	print 'Case #'+str(i+1)+': '+str(output)
				
