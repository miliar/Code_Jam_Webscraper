import sys
# r is the radius of the beginning WHITE circle
def paint(r):
	return (2*r) + 1

def solve(r, t):
	#print r, t
	paint_remaining = t
	inner_ring_radius = r
	num_rings = 0
	while(True):
		required = paint(inner_ring_radius)
		if (required > paint_remaining):
			return num_rings
		num_rings += 1
		paint_remaining -= required
		inner_ring_radius += 2

def main():
	lines = sys.stdin.readlines()
	num_cases = int(lines[0])
	for i in range(num_cases):
		l = lines[i+1].split()
		r = int(l[0])
		t = int(l[1])
		print "Case #%d: %d" % (i+1, solve(r, t))
main()