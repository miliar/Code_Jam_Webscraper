import math
import sys
from time import sleep
import copy

f = open('B-small-attempt6.in')
o = open('output.dat', 'w')

N = int(f.readline())

d = dict()

def measure_time(diners):
	global d
	# print diners

	sorted_diners = sorted(diners)
	sorted_diners_tuple = tuple(sorted_diners)
	if sorted_diners_tuple not in d:
		if len(filter(lambda t: t > 1, diners)) == 0:
			d[sorted_diners_tuple] = 1
			# print "computed:", d[sorted_diners_tuple]
		else:
			non_special_diners = map(lambda t: t - 1, sorted_diners)
			non_special_diners = filter(lambda t: t > 0, non_special_diners)

			# print 'sorted diners:', sorted_diners
			biggest = sorted_diners[-1]

			last_two_pairs = []
			for i in range(biggest):
				last_two_pairs.append([i, biggest - i])
			last_two_pairs = last_two_pairs[1:-1]
			all_possible_diners = map(lambda t: sorted_diners[:-1] + t, last_two_pairs)
			all_possible_diners = all_possible_diners + [non_special_diners]

			# print "recursing...", special_diners, non_special_diners
			d[sorted_diners_tuple] = 1 + min(map(measure_time, all_possible_diners))
	# print "found:", d[sorted_diners_tuple]
	return d[sorted_diners_tuple]

for i in range(N):
	x = f.readline()
	diners = map(int, f.readline().strip().split())
	# print diners

	# t = 0
	# print measure_time(diners)

	# print >>o, diners
	print >>o, "Case #" + str(i + 1) + ": " + str(measure_time(diners))




# for i in range(N):
# 	for line in lines[1:]:
# 		i = i + 1
# 		_, shyness = line.split(" ")

# 		s = 0
# 		m = 0
# 		for ix, el in enumerate(shyness):
# 			intel = int(el)
# 			if ix - s > m:
# 				m = ix - s
# 			s = s + intel
# 		print >>o, "Case #" + str(i) + ": " + str(m)
# 	