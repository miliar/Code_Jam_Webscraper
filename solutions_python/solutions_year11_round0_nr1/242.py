#! /usr/bin/python


if __name__ == '__main__':
	import sys
	import pdb
	
	f = open(sys.argv[1], 'r')
	
	test_cases = int(f.readline())
	for i in range(test_cases):
		
		line = f.readline().split()
		buttons = int(line[0])
		line = line[1:]

		olast,blast = 1, 1 # The locaiton of the last o/b
		osince,bsince = 0, 0 # The value moved since last o/b
		total = 0 # total movement
		prev = ""
		start = False
		for x in range(0, buttons*2, 2):
			pos = int(line[x+1]) # make it an int
			if not start: # Initial start
				start = True
				if line[x] == 'O':
					olast = pos
					osince = 0
					bsince += pos
					total += pos
				else:
					blast = pos
					bsince = 0
					osince += pos
					total += pos
			
			# On a streak
			elif line[x] == 'B' and prev == 'B':
				travel = abs(blast-pos) + 1
				blast = pos
				bsince = 0
				osince += travel
				total += travel
			elif line[x] == 'O' and prev == 'O':
				travel = abs(olast-pos) + 1
				olast = pos
				osince = 0
				bsince += travel
				total += travel
			
			elif line[x] == 'B' and prev == 'O':
				if bsince >= abs(blast - pos):
					travel = 1
				else:
					travel = abs(bsince - abs(blast - pos)) + 1
				blast = pos
				bsince = 0
				osince = travel
				total += travel

			elif line[x] == 'O' and prev == 'B':
				if osince >= abs(olast - pos):
					travel = 1
				else:
					travel = abs(osince - abs(olast - pos)) + 1
				olast = pos
				osince = 0
				bsince = travel
				total += travel

			prev = line[x]
		print 'Case #%d: %d' % ((i+1), total)
	
	f.close()
