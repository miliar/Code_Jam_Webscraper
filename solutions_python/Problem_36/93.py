count_cache = { }

def count_str_contains(line, remain_str):
	if(len(remain_str) == 1):
		return line.count(remain_str)

	if (line, remain_str) in count_cache:
		return count_cache[(line, remain_str)]

	this_char = remain_str[0]
	next_char = remain_str[1]

	occurance = 0
	this_char_cnt = 0
	next_flag = False
	for pos, c in enumerate(line):
		if c == this_char:
			this_char_cnt = this_char_cnt + 1
			next_flag = False
		elif not next_flag and c == next_char:
			occurance = occurance + ( this_char_cnt *
					count_str_contains(line[pos:], remain_str[1:]) )
			next_flag = True
			this_char_cnt = 0

	count_cache[(line, remain_str)] = occurance % 10000

	return occurance % 10000


def remove_garbage_chars(line, necessaries=[]):
	start_idx = line.find("w")
	end_idx = line.rfind("m")
	line = line[start_idx:end_idx+1]
	new_line = ""
	for character in line:
		if character in necessaries:
			new_line = new_line + character
	return new_line

if __name__ == "__main__":
	import sys

	INPUT_FILE = "C-large.in"
	welcome_str = "welcome to code jam"
	letters = [c for c in welcome_str]
	unique_letters = set(letters)

	lines = file(INPUT_FILE).read().splitlines()[1:]
	len_lines = len(lines)
	for i, l in enumerate(lines):
		count_cache = { }
		line = remove_garbage_chars(l, necessaries = unique_letters)
		result = "Case #%d: %04d" % (i+1, 
				count_str_contains(line, welcome_str))
		if i == len_lines - 1:
			sys.stdout.write(result)
		else:
			print result
