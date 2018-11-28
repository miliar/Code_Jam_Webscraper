import string

def int_input():
	return int(raw_input())

def list_int_input():
	return [int(i) for i in raw_input().split()]

def count_higher_pairs(num, a, b):
	num_str = str(num);
	count = 0;
	counted_number = {}
	for i in range(1, len(num_str)):
		new_num = int(num_str[-i:] + num_str[:-i])
		if a <= new_num and new_num <= b and num < new_num and counted_number.has_key(new_num) == False:
			count += 1
			counted_number[new_num] = True
	while num < b:
		num *= 10;
		if num <= b:
			count += 1
	return count

def solve():
	a, b = list_int_input()
	answer = 0
	for i in range(a, b+1):
		answer += count_higher_pairs(i, a, b)
	return answer

def main():
	for i in range(1, int_input()+1):
		print 'Case #%d: %s' % (i, solve())

main()