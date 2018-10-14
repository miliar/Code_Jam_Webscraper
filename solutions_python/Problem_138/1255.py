#!/usr/bin/python

import sys

def read_input(filepath):
	f = open(filepath, 'r')
	cases = int(f.readline())
	for x in xrange(1, int(cases) + 1):
		solve_prob(x, int(f.readline()), 
			[float(y) for y in f.readline().split()], 
			[float(y) for y in f.readline().split()])


def solve_prob(case, N, list1, list2):
	y = play_deceitful_war(N, list(list1), list(list2))
	z = play_war(N, list1, list2)

	print "Case #%d: %d %d" % (case, y, z)

def play_war(N, naomi, ken):
	# print "WAR"
	# print naomi
	# print ken
	# print "::::::::::::::::"


	count = 0
	for block in sorted(naomi): 
		# print "naomi choose: ", block
		ken_blocks_greater = [x for x in ken if (block < x)]
		# print "greater", ken_blocks_greater
		if not ken_blocks_greater:
			ken_blocks_greater = ken
		ken_block = min(ken_blocks_greater)
		ken.remove(ken_block)

		# print "block", block, "ken_block", ken_block
		if block > ken_block:
			count += 1
	return count


def play_deceitful_war(N, naomi, ken):
	
	# print "naomi_s", sorted(naomi)
	# print "ken_s", sorted(ken)
	# print "::::::::::::::::"
	naomi.sort()
	ken.sort()

	count = 0
	for x in xrange(N):
		if ken[-1] > naomi[-1]:
			ken.remove(ken[-1])
			naomi.remove(naomi[0])
		else:
			count += 1
			ken.remove(ken[-1])
			naomi.remove(naomi[-1])


		# print "n: ", naomi
		# print "k: ", ken
	return count

def main():
	if (len(sys.argv) < 2):
		sys.exit("usage blablabla")

	read_input(sys.argv[1])

if __name__ == '__main__':
	main()