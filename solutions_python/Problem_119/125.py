import networkx as nx
from random import randint
import sys
from countutil import *
from bisect import bisect
import itertools
import numpy
import copy
import random

locks = []
treasure_keys = []
solved = {}
shifts=[0]
blocked = set([])
for i in range(1,300):
	shifts.append((1<<(i-1)))
	
def iterate_empty(mask,nchests):
	index = 1
	for index in range(1,nchests+1):
		pos=shifts[index]
		if not mask & pos:
			yield index

def iterate_empty2(mask,nchests):
	for i in xrange(1,nchests+1):
		if not mask or not mask&1:
			yield i
		mask>>=1	

def iterate_empty3(mask,nchests):
	for i in xrange(1,nchests+1):
		if not mask or not mask&1:
			yield i
		mask>>=1
					
def update_treasures(keys,t_keys,key):
	keys[key]-=1
	for k in t_keys:
		keys[k]+=1
	keys[0]+=(len(t_keys)-1)

def undo_update(keys,t_keys,key):
	keys[key]+=1
	for k in t_keys:
		keys[k]-=1
	keys[0]-=(len(t_keys)-1)
			
def make_decision(mask,keys,total,nchests):
		
	if not keys[0] or mask in blocked:
		return 
	
	blocked.add(mask)	
	
	if mask in solved:
		print solved[mask]
		return solved[mask]
		
	""""
	print mask,nchests,total
	print keys
	print ''
	"""
	#print 'chesters'
	#print mask
	#print list(chests1)
	#print list(chests2)
	#print nchests
	#print ''
	#temp = copy.deepcopy(keys)
	for chest in iterate_empty(mask,nchests):
		#print chest,mask
		key = locks[chest]
		if keys[key]:
			
			if (total+1)==nchests:
				solved[mask] = [chest]
				return [chest]
				
			t_keys = treasure_keys[chest]
			update_treasures(keys,t_keys,key)
			pos = shifts[chest]
			
			"""
			print ''
			print 
			print 'mask',mask
			print 'mask or chest',mask | pos
			print 'keys',keys
			print 'total',total+1
			print 'nchest',nchests
			print 'chest',chest
			"""
			solution = make_decision(mask|pos,keys,total+1,nchests)
			
			if solution:
				solved[mask] = [chest] + solution
				print solved[mask]
				return solved[mask]
			undo_update(keys,t_keys,key)
			#print 'maskers',mask,keys
			
def read_input(size):
	global locks
	global treasure_keys
	global solved
	global blocked

	problem='D'
	reader = get_reader(problem,size)
	writer = get_writer(problem,size)
	cases= reader.next()
	for case in range(int(cases)):
		k,n = reader.next().strip().split()
		k = int(k)
		n = int(n)
		my_keys = [0]*(201)
		ks = reader.next().strip().split()
		for key in ks:
			key = int(key)
			my_keys[key]+=1
			my_keys[0]+=1
		treasure_keys = [0]*(n+1)
		locks = [0]*(n+1)
		solved = {}
		blocked = set([])
		for chest in range(n):
			terms = reader.next().strip().split()
			chest_key = int(terms[0])
			treasure_number = int(terms[1])
			treasure_keys[chest+1] = [int(x) for x in terms[2:]]
			locks[chest+1] = chest_key
		decision = make_decision(0,my_keys,0,n)
		if not decision:
			decision = "IMPOSSIBLE"
		else:
			decision = ' '.join([str(x) for x in decision])
		writer.write("Case #"+str(case+1)+": "+decision+'\n')
		print 'finished case ', case+1
		print ''
		print ''
	increment_count(problem,size)
	writer.close()
		
if __name__=='__main__':
	size = sys.argv[1]
	read_input(size)
