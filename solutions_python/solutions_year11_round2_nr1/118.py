# coding: utf8

import os, sys, re, string

def calc_wp(row):
	w, l = 0, 0
	matched = []
	index = 0
	for ch in row:
		if ch == '1':
			w += 1
			matched.append(index)
		elif ch == '0':
			l += 1
			matched.append(index)
		index += 1
	return float(w) / (w + l), matched

def calc_owp(wp, row, own, data):
	matched = wp[own][1]
	sum = 0
	for i in matched:
		w, l = 0, 0
		for i, ch in enumerate(data[i]):
			if i == own:
				continue
			if ch == '1':
				w += 1
			elif ch == '0':
				l += 1
		sum += float(w) / (w + l)
	return float(sum) / len(matched)		

def calc_oowp(wp, row, own, owp):
	matched = wp[own][1]
	sum = 0
	for i in matched:
		sum += owp[i]
	return float(sum) / len(matched)

def solve(N, data):
	wp = map(calc_wp, data)
	owp = map(lambda x: calc_owp(wp, data[x], x, data), xrange(N))
	oowp = map(lambda x: calc_oowp(wp, data[x], x, owp), xrange(N))
	response = map(lambda x: 0.25*wp[x][0] + 0.5*owp[x] + 0.25*oowp[x], xrange(N))
	return map(lambda x: str(x), response)

def main():
	T = int(sys.stdin.readline())
	for i in xrange(1, T + 1):
		print "Case #%d:" % i
		N = int(sys.stdin.readline())
		data = map(lambda x: sys.stdin.readline().strip(), xrange(N))
		results = solve(N, data)
		print "\n".join(results)

if __name__ == '__main__':
	main()


