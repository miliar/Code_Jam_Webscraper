#!/usr/bin/env python

def get_grids(line) :
	#print line
	n,A,B,C,D,x0,y0,M = [int(i) for i in line.split()]

	grids = []

	X = x0
	Y = y0
	#print X,Y
	grids.append( (X,Y) )
	for i in range(1,n) :
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		#print X, Y
		grids.append( (X,Y) )
	
	#print grids
	return grids

def enum_three( grids ) :
	# grids : [(0,1), (7.3), ...]
	# generator function

	for first_i in range(len(grids)) :
		first = grids[first_i]
		second_grids = grids[first_i+1:]
		#print 'second:', second_grids
		for second_i in range(len(second_grids) ):
			second = second_grids[second_i]
			third_grids = second_grids[second_i+1:]
			for third_i in range(len(third_grids)) :
				third = third_grids[third_i]
				yield (first, second,third)

def included( pos, grids ) :
	print 'pos:', pos
	for grid in grids :
		print 'grid:', grid
		if grid == pos :
			return True
	return False

def count_triangles( grids ) :

	count = 0
	# select any 3 from grids
	for p1, p2, p3 in enum_three( grids ):
		#print 'candidate:', p1,p2,p3
		# check if it's center is located at any grid point
		if ((p1[0]+p2[0]+p3[0]) % 3 ) == 0 :
			if ((p1[1]+p2[1]+p3[1]) % 3 ) == 0 :
				#print 'Found!!!'
				count += 1
	return count

def solve_single(case_id, file ):
	line = file.readline()
	grids = get_grids( line )
	
	print 'Case #%d: %d' % ( case_id, count_triangles(grids) )


def solve(file) :
	num_of_cases = int(file.readline())
	for case in range(num_of_cases) :
		solve_single(case+1, file)

if __name__ == '__main__' :

	file = open('A-small-attempt0.in', 'r')
	solve(file )

