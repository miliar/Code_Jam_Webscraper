import sys

case_num=int(sys.stdin.readline()[:-1])
bit_map = [[0 for col in range(21)] for row in range(1001)]
total_bit = [0 for i in range(21)]
def add_piece_to_map(bit_map, p, piece_arr):
	for i in range(21):
		bit_map[p][i] = int(piece_arr[p]) >> i & 0x01

def add_to_total(bit_map, p, total_bit):
	for i in range(21):
		total_bit[i] += bit_map[p][i]

def check_double(total_bit):
	for p in range(21):
		if total_bit[p] % 2 != 0:
			return False
	return True

def clear_total_bit(total_bit):
	for i in range(21):
		total_bit[i] = 0
def calc_sum_except_smallest(piece_arr, piece_num):
	sum = 0
	smallest = 100000000
	for i in range(piece_num):
		tp = int(piece_arr[i])
		sum += tp
		if tp < smallest:
			smallest = tp
	return sum-smallest

for i in range(case_num):
	clear_total_bit(total_bit)
	piece_num=int(sys.stdin.readline()[:-1])
	piece_arr = sys.stdin.readline().split(" ")
	for p in range(piece_num):
		add_piece_to_map(bit_map, p, piece_arr)
		add_to_total(bit_map, p, total_bit)	
	#check if %2 == 0
	if check_double(total_bit) == False:
		print "Case #%d: NO" % (i+1)
		continue
	res = calc_sum_except_smallest(piece_arr, piece_num)
	print "Case #%d: %d" % (i+1, res)
