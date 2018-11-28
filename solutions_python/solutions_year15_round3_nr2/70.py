#!/usr/bin/env python
import sys

K = 0
L = 0
S = 0
kd = {}
ks = ''
aim = ''

def longestReuse(s):
	i = 0
	for i in range(len(s)-1, -1, -1):
		if s[:i] == s[len(s) - i:]:
			break
	return i

def process():
	reuse = longestReuse(aim)
	bananas = (S - reuse) / (L - reuse)
	if bananas == 0:
		return 0.0
	kd = {}
	for k in ks:
		if k in kd:
			kd[k] += 1
		else:
			kd[k] = 1
	p = 1.0
	for k in aim:
		if not k in kd:
			return 0.0
		p *= (kd[k]*1.0)/K
	p *= S - L + 1
	return bananas - p

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	K, L, S = map(int, input_file.readline().split())
	ks = input_file.readline().strip()
	aim = input_file.readline().strip()
	print 'Case #%d:' % (i + 1), process()