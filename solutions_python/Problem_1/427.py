#!/usr/bin/env python

def list_find( l, find_obj, start_pos=0 ) :
	for i, j in enumerate(l) :
		if i<start_pos :continue
		if j == find_obj : return i
	return None

def find_furthest( start_pos, engines, queries ):
	furthest= 0
	cur_engine = None
	for engine in engines :
		distance = list_find( queries, engine,start_pos)
		#print 'engine', engine, 'ditance', distance
		if distance != None and distance > furthest :
			furthest = distance
			cur_engine = queries[furthest]
		elif distance == None :
			furthest = len(queries)
			cur_engine = engine

	return furthest, cur_engine

	
def min_switch_num( engines, queries ) :
	switch_cnt = 0
	cur_pos = 0 
	cur_engine = None

	while True :
		cur_pos, cur_engine = find_furthest( cur_pos, engines, queries )
		#print cur_pos, cur_engine
		if cur_pos == len(queries) :break
		switch_cnt += 1

	return switch_cnt


def solve_single( prob_num, file ) :
	num_of_engine = int( file.readline() )
	engines = []
	for i in range(num_of_engine) :
		engines.append( file.readline().rstrip() )

	num_of_query = int( file.readline() )
	queries = []
	for i in range( num_of_query )  :
		queries.append( file.readline().rstrip() )
	
	# test
	#print engines
	#print queries
	print 'Case #%d: %d' % ( prob_num, min_switch_num( engines, queries ) )

def solve( file_name ) :
	file = open( file_name , 'r' )

	num_of_cases = int( file.readline() )

	for i_prob in range(num_of_cases) :
		solve_single( i_prob+1, file )

if __name__ == '__main__' :
	
	solve( 'A-large.in' )	

