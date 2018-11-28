#!/usr/bin/python

import sys
import re

def main():
	if len(sys.argv) < 3:
		print "Needs input and output files"
		sys.exit(1)

	fin = open(sys.argv[1], 'r')
	fout = open(sys.argv[2], 'w')

	cases = int(fin.readline())

	for c in range(cases):
		s = fin.readline().strip().split(r' ')
		
		num_ins = int(s.pop(0))

		time = 0

		o_place = 1
		b_place = 1

		o_targets = []
		b_targets = []

		o_target = 1
		b_target = 1

		for i in range(len(s)):
			if s[i] == 'O':
				o_targets.append(s[i+1])
				
			elif s[i] == 'B':
				b_targets.append(s[i+1])

		o_target = int(o_targets.pop(0)) if len(o_targets) > 0 else None
		b_target = int(b_targets.pop(0)) if len(b_targets) > 0 else None

		for i in range(num_ins):
			robot = s.pop(0)
			s.pop(0) # discard

			if robot == 'O':
				time_elapsed = abs(o_target - o_place) + 1	# 1 for button press
				o_place = o_target
				o_target = int(o_targets.pop(0)) if len(o_targets) > 0 else None
				time += time_elapsed

				if b_target != None:
					if abs(b_target - b_place) < time_elapsed:
						b_place = b_target
					else:
						if b_place > b_target:
							b_place -= time_elapsed
						else:
							b_place += time_elapsed

			elif robot == 'B':
				time_elapsed = abs(b_target - b_place) + 1	# 1 for button press
				b_place = b_target
				b_target = int(b_targets.pop(0)) if len(b_targets) > 0 else None
				time += time_elapsed

				if o_target != None:
					if abs(o_target - o_place) < time_elapsed:
						o_place = o_target
					else:
						if o_place > o_target:
							o_place -= time_elapsed
						else:
							o_place += time_elapsed

		fout.write("Case #%d: %d\n" % (c + 1, time)) 

	fin.close()
	fout.close()

if __name__ == '__main__':
	main()
