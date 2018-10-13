#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
DEBUG = False
# DEBUG = True

def pd(*str):
	if DEBUG:
		print str

def main():
	lines = []
	with open(sys.argv[1], 'r') as fp:
		lines = fp.readlines()
	nmax = int(lines.pop(0))
	for n in range(nmax):
		line = lines.pop(0)
		p_str = loop(line)
		print "Case #%d: %s" % (n+1, p_str)

def loop(line_str):
	line = line_str.split()
	pd("line", line)

	c = {} # combine
	d = {} # opposed
	s = None # invoke string

	# combine
	C = int(line.pop(0))
	for i in range(C):
		_c = line.pop(0)
		c0 = min(_c[0],_c[1])
		c1 = max(_c[0],_c[1])
		assert(not c.has_key((c0,c1)))
		c[(c0, c1)] = _c[2] 
	# opposed
	D = int(line.pop(0))
	for i in range(D):
		_d = line.pop(0)
		d0 = min(_d[0],_d[1])
		d1 = max(_d[0],_d[1])
		d[(d0,d1)] = True
	# invoke string
	gomi = line.pop(0)
	s = line.pop(0)
	assert(len(line)==0)

	current_list = []
	for i in range(len(s)):
		current_list.append(s[i])
		current_list = updateCurrentList(current_list, c, d)
	
	r_str = "[" + ", ".join(current_list) + "]"
	return r_str

def updateCurrentList(list, c, d):
	if len(list)<2:
		return list
	pd('update', list, c, d)
	flag = False
	# combine
	flag, list = doCombine(list, c)
	if flag:
		return list
	# remove
	list = doRemove(list, d)
	return list

def doCombine(list, c):
	_s0 = list[-1]
	_s1 = list[-2]
	s0 = min(_s0, _s1)
	s1 = max(_s0, _s1)
	pd('s0,s1,c:', s0, s1, c)
	if c.has_key((s0,s1)):
		# print "#"*100
		list = list[:-2] + [c[s0,s1]]
		return True, list
	return False, list

def doRemove(list, d):
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			_s0 = list[i]
			_s1 = list[j]
			s0 = min(_s0, _s1)
			s1 = max(_s0, _s1)
			if d.has_key((s0,s1)):
				return []
	return list

if __name__=='__main__':
	main()
