#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('A-small-attempt2.in','r')
outf = open('Q1','w')

def main():
	t = int(f.readline())
	for x in xrange(0,t):
		judge(x)

def judge(x):
	r1 = int(f.readline())
	m1 = []
	for row in xrange(0,4):
		m1.append(f.readline().split())
	# print m1
	l1 = m1[r1-1]
	r2 = int(f.readline())
	m2 = []
	for row in xrange(0,4):
		m2.append(f.readline().split())
	l2 = m2[r2-1]
	res = judge_line(l1,l2)
	print 'Case #%d: %s'%(x+1,res)
	outf.write('Case #%d: %s\n'%(x+1,res))

def judge_line(l1,l2):
	count = 0
	res = 0
	for i1 in l1:
		for i2 in l2:
			if i1 == i2:
				count+=1
				res = i1
	if count == 1:
		return res
	if count == 0:
		return 'Volunteer cheated!'
	if count > 1:
		return 'Bad magician!'

if __name__ == '__main__':
	main()