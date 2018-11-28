import sys


def eat_motes(start_size, motes):
	calc = { 0: start_size } # dict of moves -> size 
	
	def add_to_calc(calc, moves, size):
		#print "a", moves, size
		if moves in calc:
			if size > calc[moves]:
				calc[moves] = size
		else:
			calc[moves] = size
		
	for m in motes:
		new_calc = {}
		for moves, size in calc.iteritems():
		# we have to add new mote/motes or delete next mote
			# check both
			# 1. eat:
			if size > 1: # no way to eat up from 1
				s = size
				mvs = moves
				while s <= m and mvs <= 100: # max 100 moves... possible
					s = s + s - 1
					mvs = mvs + 1
				if m < s:
					add_to_calc(new_calc, mvs, s + m)
			# 2. drop
			add_to_calc(new_calc, moves + 1, size)
		calc = new_calc
		#print calc
	
	# get minimum  moves
	min_moves = 1000
	for moves, s in calc.iteritems():
		min_moves = min(min_moves, moves)
	return min_moves
	
						

if __name__ ==  "__main__":
	f = sys.stdin
	T = int(f.readline())
	for i in xrange(1, T + 1):
		mote_size = int(f.readline().split()[0])
		motes = [int(m) for m in f.readline().split()]
		motes.sort()
		
		print  "Case #%d: %d" % (i, eat_motes(mote_size, motes))