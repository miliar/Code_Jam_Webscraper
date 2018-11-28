#!/usr/bin/env python
import sys

def trans(s):
	if s == '.': return -1;
	if s == '0': return 0;
	if s == '1': return 1;
debug = 0
f = open("A-large.in", 'r')
lines = f.readlines()
t = int(lines[0])
cur = 1
for ii in range(t):
	n = int(lines[cur])
	b = [[0 for col in range(n)] for row in range(n)]
	rpi = [0] * n
	for j in range(n):
		for k in range(n):
			b[j][k] = trans(lines[cur + 1 + j][k])

	'''for j in range(n):
		for k in range(n):
			print "b[%s][%s] = %s " %(j, k, b[j][k]),
		print  ""	
	'''
	wp = [0.0]*n
	owp = [0.0]*n
	oowp = [0.0]*n
	for j in range(n):
		wpc = 0
		for k in range(n):
			#print "b[%s][%s] = %s" %(j, k, b[j][k])
			if(b[j][k] >= 0):
				wp[j] = wp[j] + b[j][k]
				wpc = wpc + 1 
		if debug: 
			print "wpc:", wpc
			print "wp",  wp[j]
		wp[j] = wp[j]/wpc
	if  debug:
		print "wp:"
	for j in range(n):
		owpc = 0
		for k in range(n):
			if k == j or b[k][j] < 0 : 
				continue
			owpc =  owpc + 1
			oppo = 0
			count = 0
			score = 0.0
			for l in range(n):
				if l == j: continue
				oppo = oppo + 1
				if b[k][l] >= 0:
					count = count + 1
					score = score + b[k][l]
			owp[j] = owp[j] + score/count
		if owpc > 0:
			owp[j] = owp[j]/owpc

	for j in range(n):
		count = 0
		for k in range(n):
			if b[j][k] >= 0:
				count = count + 1
				oowp[j] = oowp[j] + owp[k]
		oowp[j] = oowp[j]/count
	print "Case #%s:" %(ii+1)
	for j in range(n):
		rpi[j] = 0.25*wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]
		print rpi[j]
	cur = cur + n + 1
