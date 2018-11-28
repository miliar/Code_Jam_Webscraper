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
				if num_lines < 1:
					num_lines = 1
				elif num_lines > 30:
					num_lines = 30
			elif len(lines) == num_lines:
				return lines
			else:
				if line[-1] == '\n':
					line = line[:-1]
				lines.append(line[:100])
	return lines

def create_output(results):
    f = open('output.txt', 'w')
    for i in range(len(results)):
		text = "Case #" + str(i+1) + ": " + results[i]
		print >>f, text

def create_map(input, output):
	for i in range(len(input)):
		g = input[i]
		s = output[i]
		for j in range(len(g)):
			ALPHABET_MAP[g[j]] = s[j]

def process_lines(lines):
	results = []
	for line in lines:
		new_line = ''
		for i in range(len(line)):
			new_line += ALPHABET_MAP[line[i]]
		results.append(new_line)
	return results

if __name__ == '__main__':
	script_name, input_file = sys.argv
	lines = read_input(input_file)
	create_map(['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv', 'yeqz'], ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up', 'aozq'])
	results = process_lines(lines)
	create_output(results)
	