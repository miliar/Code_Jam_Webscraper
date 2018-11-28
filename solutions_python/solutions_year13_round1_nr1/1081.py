import sys

def max_paint(r, t):
	center_white_area = r*r
	print(str(center_white_area))
	first_black_area = ((r+1)*(r+1)) - center_white_area
	print(str(first_black_area))
	last_black_area = first_black_area
	print(str(last_black_area))
	nb_black_circles = 1
	rem_paint = t - last_black_area
	print(str(rem_paint))
	while rem_paint >= 0:
		last_black_area = last_black_area + 4
		#print ('last '  + str(last_black_area))
		rem_paint = rem_paint - last_black_area
		#print ('rem '  + str(rem_paint))
		nb_black_circles += 1
		#print ('nb '  + str(nb_black_circles))
	return nb_black_circles - 1


def main(input_file_name, output_file_name):
	input_file = open(input_file_name, 'rU')
	output_file = open(output_file_name, 'w')
	for case in range(int(input_file.readline())):
		r, t = [int(x) for x in input_file.readline().split()]
		max = max_paint(r, t)
		output_file.write('Case #' + str(case+1) + ': ' + str(max) + '\n')
	input_file.close()
	output_file.close()


if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
