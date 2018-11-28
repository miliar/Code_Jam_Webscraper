import sys

def draw(r):
	return (2*r) + 1
	
out_file = open('output.out', 'w+')
in_file = open('A-small-attempt0.in', 'r+')
num_cases = int(in_file.readline())

for c in range(1, num_cases+1):
	line = in_file.readline().strip('\n').split()

	radio = int(line[0])
	paint = int(line[1])
	circles = 0
	
	painting = draw(radio)
	paint -= painting
	
	while paint >= 0:
		painting += 4
		circles += 1		
		paint -= painting
		
	case = 'Case #'+str(c)+': ' + str(circles)
	out_file.write(case+'\n')