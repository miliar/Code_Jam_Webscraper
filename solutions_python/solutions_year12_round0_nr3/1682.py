import math


def countRecycledPairs(A,B):
	count = 0
	array = []
	for i in range(A,B):
		if (i not in array):
			# print i
			numbers = checkNumber(A,B,i)

			if len(numbers) > 1:
				if (len(numbers) == 4):
					print numbers
				array.extend(numbers)
				count += combination(len(numbers), 2)
				# print count
	print count
	return count

def combination(n,r):
	return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))


def checkNumber(A,B,i):
	rotated = [i]
	string_i = "%d" % i
	length = len(string_i)
	for x in range(0, length):
		new_string = string_i[x:] + string_i[:x] 
		i_new = int(new_string)
		if (i_new >= A and i_new <= B and i_new != i):
			rotated.append(i_new)
			# print "%d" % i_new
	return rotated

def main(input_file):
	f = open(input_file, "r")
	fout = open("%s.out" % input_file, "w")
	max_lines = int(f.readline())
	for line_number in range(0,max_lines):
		line = f.readline().strip()
		line_split = line.split(" ")
		A = int(line_split[0])
		B = int(line_split[1])
		count = countRecycledPairs(A,B)
		output_line = "Case #%d: %d\n" % (line_number + 1, count) 
		print output_line
		fout.write(output_line)

if __name__ == '__main__':
	# countRecycledPairs(1111, 2222)
	# print combination(4,2)
	# main("input_test.in")
	main("C-small-attempt0.in")







