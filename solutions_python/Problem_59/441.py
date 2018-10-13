#!/usr/bin/python

import time
count = 0

def solve():
	T = int(raw_input())
	
	global count
	
	i = 0
	while i < T:
		N, M = raw_input().split(' ')
		
		count = 0
		created_dir = []
		
		j = 0
		while j < int(N):
			dirs = raw_input().split('/')
			
			save_list(created_dir, dirs)		
		
			j += 1
			
			
		j = 0
		while j < int(M):
			dirs = raw_input().split('/')
			
			p = '/'.join(dirs)
			if not check_list(created_dir, dirs):
				created_dir.append(p)
				count += 1
				
		
			j += 1
	
		print "Case #" + str(i+1) + ":", count
	
		i += 1
		

def check_list(l, path):
	global count

	p = '/'.join(path)
	if p == '/' or p == '': return True
	
	if check_list(l, path[:-1]):
		for i in l:
			if i == p: 
				return True
		else:
			l.append(p)
			count += 1
			return True
		
		return False
		
def save_list(l, path):	
	p = '/'.join(path)
	if p == '/' or p == '': return
	
	save_list(l, path[:-1])
	l.append('/'.join(path))


solve()
