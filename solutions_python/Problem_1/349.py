#!/usr/bin/env python

## google code jam

# solver for universe problem
# cat problem_data.txt | ./universe.py

# author: seanj@xyke.com

import sys, string

"""

We find the solution by walking the list of queries
and for each query we remove it from the list of allowable
servers. 

If the list goes to zero we will have to make a switch.

The last element that we encountered is the longest run before
a switch. Add this element to the list of server choices.

Refill the list of allowable servers and continue.

"""

class ServerChoiceBucket:
	def __init__(self, servers=[]):
		self._initial_values = dict.fromkeys( list(servers), 1)
		self._working_values = {}
		self._choices = []
		self.refill()
		
	def refill( self):
		self._working_values = dict.copy( self._initial_values)

	def remove( self, item):
		try:
			self._working_values.pop( item)
		except KeyError:
			# we don't care when the item doesn't exist
			# we only care when the bucket goes to zero
			pass
			
		if len( self._working_values) == 0:
			# we have emptied the bucket, set the choice and refill
			self._choices.append( item)
			self.refill()
			self.remove( item)
			
	def empty( self):
		# got to the end, throw a choice in the list to finish up
		self._choices.append( self._working_values.popitem()[0])
		
	def get_choices( self):
		return self._choices[:]


def get_cases( f, n):
	"""read the int <n> cases from the file <f>
	
	returning a list of tuples ( servers{}, queries[] )
	[ (map, list), ... ]
	"""
	def sr():
		"strip and read from f"
		## this will remove leading and trailing spaces
		# if they are trying to bite us ...
		raw_line = f.readline()
		assert raw_line[-2] != ' '
		assert raw_line[-2] != '\t'
		return string.strip( raw_line)
		
	case_list = []
	for x in range(n):
	
		## extract the servers
		num_servers = int( sr())
		# server list need not be ordered, dict allows for quick
		# check if the query is actually a server
		servers = {}
		for x in range( num_servers):
			servers[ sr()] = 1
		assert len(servers) == num_servers
	
		## extract the queries
		num_queries = int( sr())
		query_list = []
		for x in range( num_queries):
			query = sr()
			if query not in servers:
				# if the query is not an engine we do not care about it
				# for the switch calcuations
				pass
			else:
				if len(query_list) > 0 and query_list[-1] == query:
					# we don't need to enter duplicate queries
					pass
				else:
					# new query, different from the last
					query_list.append( query)
		
		case_list.append( ( list(servers), query_list) )

	# [ ( map, list), ... ]
	return case_list

def dump_test_cases( case_l):
	for engines, queries in case_l:
		print 'engines', engines.keys()
		print 'queries', queries


if __name__ == '__main__':
	input_file = sys.stdin
	num_cases = int( input_file.readline())

	# print 'number of test cases', num_cases
	cases = get_cases( input_file, num_cases)

	for i,case in enumerate(cases):
		print 'Case #%d:' % (i+1),
		servers = case[0]
		queries = case[1]
		scb = ServerChoiceBucket( servers)
		for q in queries:
			scb.remove( q)
		scb.empty()
		choices = scb.get_choices()
		#print choices, len(choices) -1
		print len(choices) - 1
	 











































































































	

