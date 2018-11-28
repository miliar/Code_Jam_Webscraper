import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_MAP = {}

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

def process_contests(contests):
	results = []
	for n, s, p, t in contests:
		scores = []
		for ti in t:
			if ti >= p:
				scores.append(p*3 - ti)
		unsurprising = [score for score in scores if score <= 2]
		surprising = [score for score in scores if score <= 4 and score > 2]
		if len(surprising) > s:
			results.append(len(unsurprising)+s)
		else:
			results.append(len(unsurprising)+len(surprising))
	return results

def create_contests(lines):
	contests = []
	for line in lines:
		values = [int(i) for i in line.split(' ')]
		contests.append((values[0], values[1], values[2], values[3:3+values[0]]))
	return contests

if __name__ == '__main__':
	script_name, input_file = sys.argv
	lines = read_input(input_file)
	contests = create_contests(lines)
	results = process_contests(contests)
	create_output(results)
	