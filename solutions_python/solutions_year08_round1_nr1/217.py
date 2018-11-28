#!/usr/bin/env python

def get_scalar_product( v1, v2 ) :
	scalar_product = 0
	if len(v1) == len(v2):
		for i in range(len(v1)) :
			scalar_product += v1[i]*v2[i]
	return scalar_product

def get_permutated_vector( v ) :
	ret_vec = []

	#print 'v:', v

	if len(v) == 1 :
		#print 'ret_vec:', [v]
		return [v]

	for i in range(len(v)) :
		v_item = v[i]
		#print 'v_item:', v_item
		v_rest = [ v[j] for j in range(len(v)) if not j==i ]
		#print 'v_rest:', v_rest

		rest_permutation = get_permutated_vector(v_rest)
		#print 'rest_pem', rest_permutation
		for rest_item in rest_permutation :
			#print 'rest_item:', rest_item
			ret_vec.append( [v_item] + rest_item )
	
	#print 'ret_vec:', ret_vec
	return ret_vec
	

def get_min_scalar_product( v1, v2 ) :

	min_product = get_scalar_product(v1, v2)

	v2_perm = get_permutated_vector( v2 )
	#print 'permuted vec', v2_perm
	for v2_item in v2_perm :
		trial = get_scalar_product( v1, v2_item)
		if trial < min_product :
			min_product = trial
	
	return min_product

def solve_single( i, file ) :
	elem_num = int( file.readline() )
	#print elem_num
	str_v1 = file.readline().split()
	v1 = [ int(v) for v in str_v1 ]
	#print v1
	str_v2 = file.readline().split()
	v2 = [ int(v) for v in str_v2 ]
	#print v2

	print 'Case #%d: %d' % (i,get_min_scalar_product(v1,v2)) 

	# do permutation


def solve(file ) :
	num_of_case = file.readline()
	num_of_case = int(num_of_case)
	#print num_of_case
	for i in range(num_of_case) :
		solve_single(i+1, file)


if __name__ == '__main__' :
	file = open( 'A-small-attempt0.in', 'r')
	solve(file)

