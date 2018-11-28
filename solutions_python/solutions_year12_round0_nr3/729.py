import sys

LIMIT = 2000000
MAP = {};

def read_input(filename):
	lines = []
	num_lines = 0
	with open(filename) as f:
		for line in f:
			if num_lines == 0:
				num_lines = int(line)
			elif len(lines) == num_lines:
				return lines
			else:
				if line[-1] == '\n':
					line = line[:-1]
				lines.append(line)
	return lines

def create_output(results):
    f = open('output.txt', 'w')
    for i in range(len(results)):
		text = "Case #" + str(i+1) + ": " + str(results[i])
		print >>f, text

def process(problems):
	results = []	
	for a, b in problems:
		values = []
		for i in range(a,b+1):
			for num in MAP[i]:
				if a <= num and num <= b:
					values.append((i,num))
		value_set = set(values)
		results.append(len(value_set))
	return results

def create_problems(lines):
	problems = []
	for line in lines:
		values = [int(i) for i in line.split(' ')]
		problems.append((values[0], values[1]))
	return problems

def precalculate():
	def num_length(num):
		length = 0
		while num > 0:
			length += 1
			num /= 10
		return length
	def rotate(num, places):
		mod = 10**places
		mult = 10**(num_length(num)-places)
		first = num%mod * mult
		last = num/mod
		return last+first
	for i in range(1,LIMIT+1):
		MAP[i] = []
		for j in range(num_length(i)):
			num = rotate(i,j)
			if i < num:
				MAP[i].append(num)

if __name__ == '__main__':
	script_name, input_file = sys.argv
	lines = read_input(input_file)
	problems = create_problems(lines)
	precalculate()
	results = process(problems)
	create_output(results)
	