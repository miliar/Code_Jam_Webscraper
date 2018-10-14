#!/usr/bin/env python3.1

import sys

def calc(values):
	d = []
	for line in values:
		r = []
		for p in line:
			r.append(p)
		d.append(r)
	wp = []
	wp_except = []
	for r in d:
		excpt = []
		win = r.count("1")
		ttl = r.count("0") + r.count("1")
		wp.append(win / ttl)
		for p in r:
			if p == ".":
				excpt.append(win / ttl)
			elif p == "0":
				excpt.append(win / (ttl - 1))
			else:
				excpt.append((win - 1) / (ttl - 1))
		wp_except.append(excpt)
	owp = []
	for i in range(len(d)):
		ttl = 0
		cnt = 0
		for o in range(len(d)):
			if d[i][o] != '.':
				cnt += 1
				ttl += wp_except[o][i]
		owp.append(ttl / cnt)
	oowp = []
	for i in range(len(d)):
		ttl = 0
		cnt = 0
		for o in range(len(d)):
			if d[i][o] != '.':
				cnt += 1
				ttl += owp[o]
		oowp.append(ttl / cnt)
	for i in range(len(d)):
		print("%f" % (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]))

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	numLines = getints()[0]
	print("Case #%d:" % (i+1))
	result = calc([sys.stdin.readline().strip() for x in range(numLines)])
