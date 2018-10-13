
import sys 
import itertools


def cal_cost(char_lists):

	n_chars = len(char_lists[0])
	if any( len(l) != n_chars for l in char_lists):
		return -1
	
	cost = 0
	for i in range(n_chars):
		char = char_lists[0][i][0]
		if any( l[i][0] != char for l in char_lists):
			return -1

		longest = max((l[i][1] for l in char_lists))
		shortest = min((l[i][1] for l in char_lists))
		cost += (longest - shortest)

	return cost

t = int(sys.stdin.readline())

for case in range(1, t+1):
	
	n = int(sys.stdin.readline())
	char_lists = []
	for i in xrange(n):
		line  = sys.stdin.readline()
		#print line
		char_list = []

		char_count = 0
		last_char  = line[0]
		for s in line:
			if s == last_char:
				char_count += 1
			else:
				char_list.append( (last_char, char_count) )
				last_char = s
				char_count = 1
		char_list.append( (last_char, char_count) )
		#print char_list

		char_lists.append(char_list)

	cost = cal_cost(char_lists)
	if cost < 0:
		print "Case #{0}: {1}".format(case, 'Fegla Won')
	else:
		print "Case #{0}: {1}".format(case, cost)



