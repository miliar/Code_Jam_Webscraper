# dominos

X = 2
R = 2
C = 2


def domino_tile(X,R,C):

	# see if the number of dominos just don't fit on the grid
	if X > R and X > C:
		return "RICHARD"
		
	# see if there exists one that doesn't fit
	all_hulls = [(k,X-k+1) for k in range(1,X+1)]
	for hull in all_hulls:
		if (hull[0] > R and hull[1] > R) or (hull[0] > C and hull[1] > C):
			return "RICHARD"
	
	
	# make sure it can be tiled at all
	area = R*C
	if area < X or area % X != 0:
		return "RICHARD"
		
	# see if ricky can force any holes of size <= X
	
	# case 1: choose a domino with a hole in it. if X >= 7 and R,C >= 3 this is possible
	if X >= 7 and R >= 3 and C >= 3:
		return "RICHARD"
		
	# case 2: hole against the edge of the board somewhere?
	allowable_hulls = [(k,X-k+1) for k in range(1,X+1) if (k <= R and X-k+1 <= C)]
	if allowable_hulls:
		hull_volume = max( allowable_hulls )
	else:
		hull_volume = 0
		
	for hull in allowable_hulls:
		if hull[0] == R:
			# potentially blocking
			# see if we can separate the volume into regions of bad areas for tiling
			deficit = hull[0] * hull[1] - X
			# can separate the area into regions with n*R + d and n*R+(deficit-d) area, 
			# for some integer 0<=n<=C-hull[1] and 0<=d<=deficit
			
			# slide the tile along and see what we can do
			for d in range(deficit+1):
				# need to find a d such that it's untileable for all n
				untileable = True
				for n in range(C - hull[1] + 1):
					l_volume = n*hull[0] + d
					r_volume = (C-n-hull[1])*hull[0] + (deficit - d)
					if l_volume % X == 0 and r_volume % X == 0:
						untileable = False
				if untileable:
					return "RICHARD"
		if hull[1] == C:
			# potentially blocking
			# see if we can separate the volume into regions of bad areas for tiling
			deficit = hull[0] * hull[1] - X
			# can separate the area into regions with n*R + d and n*R+(deficit-d) area, 
			# for some integer 0<=n<=C-hull[1] and 0<=d<=deficit
			
			# slide the tile along and see what we can do
			for d in range(deficit+1):
				# need to find a d such that it's untileable for all n
				untileable = True
				for n in range(R - hull[0] + 1):
					l_volume = n*hull[1] + d
					r_volume = (R-n-hull[0])*hull[1] + (deficit - d)
					if l_volume % X == 0 and r_volume % X == 0:
						untileable = False
				if untileable:
					return "RICHARD"
		
	return "GABRIEL"
	
def check(line):
	data = [int(x) for x in line.split()]
	return domino_tile(data[0], data[1], data[2])
		
with open("4.in") as f:
	lines = [l.strip() for l in f]
	
ncases = int(lines[0])

for i in range(1, ncases + 1):
	data = [int(x) for x in lines[i].split()]
	X = data[0];
	R = data[1];
	C = data[2];
	
	print("Case #{0}: {1}".format(i, domino_tile(X,R,C)))
