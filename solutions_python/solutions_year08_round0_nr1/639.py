import string
import sys
import math




#Optimization I intend to try:
#	Cache trees on various depths.
#	Then if the criteria matches there's no need to re-derive it, just use a cached version.


tree_cache = {}

#Build key for a tree at depth query_idx, with root node starting at [query, engine]
def getTreeKey(query_idx, query, engine):
	return str(query_idx)+':'+query+':'+engine



#-----------
def buildTree(current_node, query_idx, engine, engines, queries):
	if len(queries) <= query_idx:
		return
		
	#print current_node
		
	current_query = queries[query_idx]
	query_idx += 1
	#print 'examine query = ',current_query
	#print 'query index = ',query_idx
	
	if current_query == engine:
		#a branch point.
		#branch out to all possibilities.
		#print 'branch point from engine = ',engine,' at query ',current_query
		for tmp_engine in engines:
			if tmp_engine != current_query:
				new_node = [None, None, current_query, tmp_engine]
				
				tree_key = getTreeKey(query_idx, current_query, tmp_engine)
				
				if tree_cache.has_key(tree_key):
					new_node = tree_cache[tree_key]
				else:
					buildTree(new_node, query_idx, tmp_engine, engines, queries)
					tree_cache[tree_key] = new_node
					
				#Attach the subtree to this one.
				if current_node[1] is None:
					current_node[1] = []
				current_node[1].append(new_node)
	else:
		#keep on adding left nodes while this engine is suitable.
		#print 'left node'
		new_node = [None, None, current_query, engine]
		
		if current_node[0] is None:
			current_node[0] = []
		current_node[0].append(new_node)
		buildTree(current_node, query_idx, engine, engines, queries)
		#current_node[0] = new_node
		#buildTree(new_node, query_idx, engine, engines, queries)
		
		

#-----------
def printTree(current_node, indent):
	#line = '-' * indent + '>ENGINE:' + str(current_node[3]) + '( "' + str(current_node[2]) + '" )'
	line = '-' * indent + '>ENGINE:' + str(current_node[3]) + '( "' + str(current_node[2]) + '" )'
	print line
	
	#left nodes are just data. not for traversal.
	
	if current_node[1] is not None:
		tmp_indent = indent
		for node in current_node[1]:
			tmp_indent = tmp_indent + 3
			printTree(node, tmp_indent)
	
	
	#if current_node[0] is not None:
	#	printTree(current_node[0], indent)
	#	
	#if current_node[1] is not None:
	#	tmp_indent = indent
	#	for node in current_node[1]:
	#		tmp_indent = tmp_indent + 5
	#		printTree(node, tmp_indent)
	
	
#-----------


def calculateTreeDepth(current_node, depth, min_depth, query_idx):
	#left nodes are just data. not for traversal.
	
	#bail out if the current minimum is already equaled or exceeded.
	#if depth >= min_depth[0]:
	#	return
		
	#print 'query_idx = ',query_idx,' min_depth[0] = ',min_depth[0]
	
	if current_node[0] is not None:
		query_idx = query_idx + len(current_node[0])
		
	
	if current_node[1] is not None:
		for node in current_node[1]:
			
			result = None
			depth_key = getMinDepthKey(node[2], node[3], query_idx, depth+1)
			
			if mindepth_cache.has_key(depth_key):
				result = mindepth_cache[depth_key]
			else:
				calculateTreeDepth(node, depth+1, min_depth, query_idx)
				mindepth_cache[depth_key] = min_depth[0]
			
			if result is not None:
				if result < min_depth[0]:
					min_depth[0] = result
			
			#calculateTreeDepth(node, depth+1, min_depth)
	else:
		#a leaf node.
		#update the current minimum total.
		if depth < min_depth[0]:
			min_depth[0] = depth
	

#-----------


mindepth_cache = {}

#Build key for a tree at depth query_idx, with root node starting at [query, engine]
def getMinDepthKey(query, engine, query_idx, depth):
	return str(query_idx)+':'+query+':'+engine+':'+str(depth)



def countMinDepth(current_node, depth):
	min_depth = 50000000000
	
	
	if current_node[0] is not None:
	
		#result = None
		#depth_key = getMinDepthKey(current_node[2], current_node[3], depth)
		
		#if mindepth_cache.has_key(depth_key):
		#	result = mindepth_cache[depth_key]
		#else:
		result = countMinDepth(current_node[0], depth)
		#mindepth_cache[depth_key] = result
			
		if result < min_depth:
			min_depth = result
		
		
	if current_node[1] is not None:
		#child nodes that branch off for different engines.
		#print 'subnodes in list: ',len(current_node[1])
		for node in current_node[1]:
			
			result = None
			depth_key = getMinDepthKey(node[2], node[3], depth)
			
			#print depth_key
			
			if mindepth_cache.has_key(depth_key):
				result = mindepth_cache[depth_key]
			else:
				result = countMinDepth(node, depth+1)
				mindepth_cache[depth_key] = result
				
			if result is not None:
				if result < min_depth:
					min_depth = result
					
	
	if current_node[0] is None and current_node[1] is None:
		#a leaf node therefore
		#print 'leaf'
		return depth
	
	return min_depth
	
	

	


#import psyco
#psyco.full()



#--------------------------------------------

if len(sys.argv) < 2:
	print 'Specify input filename'
	sys.exit(0)

filename = sys.argv[1]
input_file = open(filename)

line = input_file.readline()
num_cases = string.atoi(line)

for case_nr in range(1,num_cases+1):
	engines = []
	
	num_engines = int(input_file.readline())
	for a in range(0, num_engines):
		engines.append( input_file.readline() )
	
	queries = []
	num_queries = int(input_file.readline())
	for a in range(0, num_queries):
		queries.append( input_file.readline() )
	
	
	#Get rid of CRLFs
	for idx in range(0, len(engines)):
		engines[idx] = string.replace(engines[idx], chr(13), '')
		engines[idx] = string.replace(engines[idx], chr(10), '')
	for idx in range(0, len(queries)):
		queries[idx] = string.replace(queries[idx], chr(13), '')
		queries[idx] = string.replace(queries[idx], chr(10), '')
	


#	print engines
#	print queries
	
#	print len(engines),' engines.'
#	print len(queries),' queries.'
	
#	sys.exit(0)

	
	#Figure out the minimum number of search engine switches to avoid collisions between engine name and query.
	#One approach is a brute force method which just tries every possible switch out.
	#Probably building a sequence tree will do the trick...
	#The tree forks to the right at every search engine switch. Otherwise it is just left children connecting to each other.
	
	trees = []
	for engine in engines:
	
		rootnode = None  #[leftchild, rightchildren[], query, engine]
		
		if len(queries) > 0:
			query = queries[0]
			
			if query != engine:
				#Proceed to build a tree using this engine.
				#print '------BEGIN a tree based on engine ',engine
				rootnode = [None, None, queries[0], engine]
				
				buildTree(rootnode, 1, engine, engines, queries)
				
				#print 'done building tree.'
				#print '==========================='
				#printTree(rootnode, 0)
				#print ''
				
				#if case_nr == 16:
				#	printTree(rootnode, 0)
				
				#print 'min depth = ',countMinDepth(rootnode, 0)
				
				trees.append(rootnode)
				
			else:
				#Bail on this engine, it cannot be a root.
				#print 'bail on engine ',engine,' cause queries begin with ',query
				pass

	#print 'TOTAL trees for case: ',len(trees)
	
	min_count = [5000000000000]
	if len(trees) == 0:
		min_count[0] = 0
	for tree_root in trees:
		calculateTreeDepth(tree_root, 0, min_count, 0)
	print 'Case #' + str(case_nr) + ': ' + str(min_count[0])


	#if case_nr > 4:
	#	sys.exit(0)

		
	