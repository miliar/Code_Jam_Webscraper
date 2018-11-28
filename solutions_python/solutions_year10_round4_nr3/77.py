import psyco
from sys import stdin
from sys import stderr 

psyco.full()

def get_int_arr():
	return [int(x) for x in stdin.readline().split(' ')]


def solve():
	R = int(stdin.readline())

	m = {}
	for i in range(R):
		x1, y1, x2, y2 = get_int_arr()
		for x in range(x1, x2+1):
			for y in range(y1, y2+1):
				m[(x, y)] = 1
	#print 'bac = ', len(m)
	#print m

	seconds = 0
	while len(m) > 0:
		#print seconds
		seconds += 1

		# new born map
		new_born = {}
		die_map = []
		
		for (x, y) in m.keys():
			# check die condition
			if not m.has_key((x-1, y)):		# west
				if not m.has_key((x, y-1)):	# north
					die_map.append((x, y))
			# new born condition
			if not new_born.has_key((x+1, y)):
				new_born[(x+1, y)] = 1
			else:
				new_born[(x+1, y)] += 1
			if not new_born.has_key((x, y+1)):
				new_born[(x, y+1)] = 1
			else:
				new_born[(x, y+1)] += 1
		
		#print new_born
		#print die_map
		for (x, y) in new_born.keys():
			if new_born[(x, y)] == 2:
				m[(x, y)] = 1
		for (x, y) in die_map:
			del m[(x, y)]
		#print m

	print seconds

T = int(stdin.readline())
for case in range(T):
	stderr.write("%d\n" % case)
	stderr.flush()
	print 'Case #%d:' % (case+1),
	solve()
