import math

def solve(N, K):
	N = int(N)
	K = int(K)

	big_value = N
	#small_value = None
	num_big = 1

	nodes_in_level = 1
	total_nodes = 1
	total_nodes_before = 0
	level = 0
	while total_nodes < K:

		if big_value % 2 == 0:
			pass
		else:
			num_big = 2 * num_big + 1 * (nodes_in_level - num_big)

		#print "num_big: %d" % num_big

		nodes_in_level = 2 * nodes_in_level
		level += 1
		total_nodes_before = total_nodes
		total_nodes += nodes_in_level

		big_value = big_value / 2
		#print total_nodes

	node_offset_in_level = K - total_nodes_before
	space_size =  big_value if node_offset_in_level <= num_big else big_value - 1
	
	# print node_offset_in_level
	# print num_big
	
	Max = space_size / 2
	Min = (space_size-1) / 2
	return (Max, Min)

def process_file(fname):
	f = open(fname, 'r')
	fo = open(fname + ".result", "w")

	lines = f.readlines()
	lines = [i.strip() for i in lines]

	num_samples = int(lines[0])
	lines = lines[1:]

	print("there are: %i samples" % num_samples)
	print("")

	case_num = 1
	for l in lines:
		Max, Min = solve(*l.split(' '))
		to_print = "Case #%i: %d %d\n" % (case_num, Max, Min)
		fo.write(to_print)
		case_num += 1

#process_file('sample.txt')
process_file('C-small-1-attempt0.in')
process_file('C-small-2-attempt0.in')
process_file('C-large.in')

#print solve(500, 5) # 1 0