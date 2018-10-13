import random
import math

T = int(raw_input().strip())

def dist(a, b):
	return (a[0]-b[0])**2 + (a[1]-b[1])**2

for nCase in xrange(1, T+1):
	N, W, L = map(int, raw_input().strip().split())
	r = map(int, raw_input().strip().split())
	
	valid = False
	
	while not valid:
	
		students = [(random.randint(0, W * 100) / 100.0, random.randint(0, L * 100) / 100.0) for i in xrange(N)]
	
		for rnd in xrange(1000):
			valid = True
		
			for i in xrange(N):
				for j in xrange(N):
					if i == j: continue
					if dist(students[i], students[j]) <= (r[i] + r[j])**2:
						valid = False
						
						# relax
						midpoint = ((students[i][0] + students[j][0]) / 2.0, (students[i][1] + students[j][1]) / 2.0)
					
						angle = math.atan2(students[i][1] - midpoint[1], students[i][0] - midpoint[0])	
						students[i] = (
							max(0, min(W, midpoint[0] + (r[i] + r[j])/2 * math.cos(angle))),
							max(0, min(L, midpoint[1] + (r[i] + r[j])/2 * math.sin(angle)))
						)
					
						angle = math.atan2(students[j][1] - midpoint[1], students[j][0] - midpoint[0])	
						students[j] = (
							max(0, min(W, midpoint[0] + (r[i] + r[j])/2 * math.cos(angle))),
							max(0, min(L, midpoint[1] + (r[i] + r[j])/2 * math.sin(angle)))
						)
			if valid:
				break
		
	
	print "Case #%d: %s" % (nCase, " ".join(["%f %f" % student for student in students]))

