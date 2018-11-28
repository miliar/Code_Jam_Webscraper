#! /usr/bin/python

from cStringIO import StringIO
from sys import stdin, setrecursionlimit as recdepth
import re

def make_tree(string, i):
	#print string[i:]
	while i <len(string) and (string[i]=='(' or string[i]==' ' or string[i]==')'):
		i+=1
	if i==len(string):
		return None
	space_index=string.find(' ',i)
	closing_index=string.find(')',i)
	if space_index==-1 or space_index>closing_index:
		closing=string.find(')',i)
		value=float(string[i:closing])
		#print "got %f"%value
		return ((value,),closing+1)
	else:
		#has a label
		prob=float(string[i:space_index])
		i,space_index=space_index,string.find('(', space_index+1)
		label=string[i+1:space_index]
		#print "prob=%f label=%s"%(prob,label)
		left_child,next=make_tree(string,space_index+1)
		right_child,next=make_tree(string,next)
		return ((prob,label,left_child,right_child), next)
		
def cuteness(node, traits):
	#print node
	if node==None:
		return 1.0
	elif len(node)==1:
		return node[0]
	else:
		ret,trait=node[0],node[1]
		if trait in traits:
			return ret*cuteness(node[2],traits)
		else:
			return ret*cuteness(node[3],traits)

if __name__=='__main__':
	recdepth(100000)
	data=StringIO(stdin.read())
	N=int(data.readline())
	for case in xrange(1,N+1):
		L=int(data.readline())
		string=' '.join([data.readline() for i in xrange(L)])
		string=re.sub(r'\s+',' ',string)
		string=re.sub(r'\s+\(','(', string)
		string=re.sub(r'\(\s+','(', string)
		string=re.sub(r'\s+\)',')', string)
		string=re.sub(r'\)\s+',')', string)
		#print string
		root=make_tree(string,0)[0]
		A=int(data.readline())
		print "Case #%d:"%case
		for animal in xrange(A):
			info=data.readline().split()
			traits=set(info[2:])
			print "%.7f"%cuteness(root,traits)
