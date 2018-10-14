import networkx as nx
from random import randint
import sys
from countutil import *
from bisect import bisect
import itertools
import numpy as np

def change_grid(changeMatrix,fullMatrix,new_mini):
	length = fullMatrix.shape[0]
	width = fullMatrix.shape[1]
	for change in changeMatrix:
		dim,index = change
		fullMatrix = np.insert(fullMatrix,index,new_mini,axis=dim)
		fullMatrix = np.delete(fullMatrix,index+1,axis=dim)
	return fullMatrix
	
def infer_mingrids(x,mini):
	
	changeMatrix = []
	length = x.shape[0]
	width = x.shape[1]
	for i in range(length):
		if x[i,].sum()==(mini*width):
			changeMatrix.append([0,i])
	
	t = x.transpose()
	for i in range(width):
		if t[i,].sum()==(mini*length):
			changeMatrix.append([1,i])
	
	return changeMatrix
		
def uniform(x,mini):
	return x.sum()/mini == x.size
		
def make_decision(x,minis):
	print 'starting'
	new_mini = minis[0]
	for index in range(len(minis)-1):
		mini,new_mini = minis[index],minis[index+1]
		print index,'before',x
		changeMatrix = infer_mingrids(x,mini)
		print 'changeMatrix',changeMatrix,'new_mini',new_mini
		if not changeMatrix:
			break
		x = change_grid(changeMatrix,x,new_mini)
		print index,'after',x
		print ''
	return 'YES' if uniform(x,new_mini) else 'NO'
		
def read_input(size):
	problem='B'
	reader = get_reader(problem,size)
	writer = get_writer(problem,size)
	cases= reader.next()
	for case in range(int(cases)):
		n,m = reader.next().strip().split()
		n = int(n)
		m = int(m)
		minis = set([])
		matrix = []
		for _ in range(n):
			nums = [int(x) for x in reader.next().strip().split()]
			minis=minis.union(nums)
			matrix.append(nums)
		x = np.array(matrix,np.int32)
		decision = make_decision(x,sorted(list(minis)))
		print 'input',x
		print 'decision',decision
		print ''
		writer.write( "Case #"+str(case+1)+": "+decision+'\n')
	increment_count(problem,size)
	writer.close()
		
if __name__=='__main__':
	size = sys.argv[1]
	read_input(size)