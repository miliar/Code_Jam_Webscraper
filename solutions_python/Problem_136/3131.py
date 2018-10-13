#!/usr/bin/env python

def main():
	size = "large"

	in_file = "in_{}.txt".format(size)
	out_file = "out_{}.txt".format(size)

	f = open(in_file, 'r')
	o = open(out_file, 'w')

	cases = int(f.readline().rstrip())

	for c in range(cases):
		line = map(float, f.readline().rstrip().split())
		farm_price, farm_cps, goal = tuple(line)
		
		cps = 2.0
		farms = 0
		current_time = goal / cps
		partial_time = 0

		while True:
			partial_time += farm_price / cps
			farms += 1
			cps = 2.0 + farms * farm_cps
			new_time = goal / cps

			if partial_time + new_time < current_time:
				current_time = new_time + partial_time
			else:
				break

		o.write("Case #{0}: {1}\n".format(c+1, current_time))
		print "Case #{0}: {1}".format(c+1, current_time)


main()