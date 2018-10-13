import sys

search_string = "welcome to code jam";
counts = [];

def recurse(line, start, end, search_char_index):
	global counts;

	if start > end:
		return 0;

	if search_char_index == len(search_string):
		return 1;

	sum = 0;
	for i in range(end, start - 1, -1):
		if line[i] == search_string[search_char_index]:
			if counts[i][search_char_index] == 0:
				counts[i][search_char_index] = recurse(line, i + 1, end, search_char_index + 1);
			sum += counts[i][search_char_index];
	return sum;

def do_line(case):
	line = sys.stdin.readline();

	global counts;
	counts = [];

	for i in range(len(line)):
		counts.append([0 for char in search_string]);

	print("Case #%d: %04d" % (case, recurse(line, 0, len(line) - 1, 0)));

def main():
	num_cases = int(sys.stdin.readline());

	for case in range(num_cases):
		do_line(case + 1);

main();

