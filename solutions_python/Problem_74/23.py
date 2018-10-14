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
		loop(n, line)

def parseLine(_line):
	'''
	@param[out] N:       
	@param[out] r_value: list of [char, pos]
	'''
	line = _line.split()
	N = int(line.pop(0))
	r_value = []
	for i in range(N):
		c = line.pop(0) # next charactor
		b = int(line.pop(0)) # button number
		r_value.append( (c,b) )
	return N, r_value

def nextPos(line, char):
	for c, p in line:
		if c==char:
			return p
	return 0

def updateWaitPos(Wait, pbt):
	diff = Wait['next'] - Wait['pos']
	pd("updateWaitPos", Wait, pbt)
	# if diff==0:
	# 	return
	if diff>0:
		if pbt > diff:
			Wait['pos'] = Wait['next']
		else:
			Wait['pos'] += pbt
	elif diff<0:
		if pbt > abs(diff):
			Wait['pos'] = Wait['next']
		else:
			Wait['pos'] -= pbt
	pd("->", Wait, pbt)


def loop(n, _line):
	u'''
	@param[out] かかった時間
	'''
	O = {'next':0, 'pos':1, 'char':'O'}
	B = {'next':0, 'pos':1, 'char':'B'}
	total_time = 0

	bn, line = parseLine(_line)
	for i in range(bn):
		c, b = line.pop(0) # next charactor # button number

		Next = O if c=='O' else B
		Wait = O if c=='B' else B

		Next['next'] = b
		Wait['next'] = nextPos(line, Wait['char'])

		pbt = abs(Next['next'] - Next['pos']) + 1 # push button time
		pd( '%d %d %d' % (pbt, Next['next'], Next['pos']) )

		# update position
		Next['pos'] = Next['next']
		updateWaitPos(Wait, pbt)
		total_time += pbt
		pd( '%02d O:%d B:%d' % (total_time, O['pos'], B['pos']) )
	
	print 'Case #%d: %d' % (n+1, total_time)
	return total_time


if __name__=='__main__':
	main()
