#!/usr/bin/python

import copy

n = input()
for i in xrange(n):
	t = 0
	tate,yoko = map(int,raw_input().split(" "))
	table = [[ "" for _ in xrange(yoko)] for __ in xrange(tate)]
	for j in xrange(tate):
		tmp = raw_input()
		for k in xrange(yoko):
			table[j][k] = tmp[k]

	for j in xrange(1,tate):
		for k in xrange(1,yoko):
			if table[j][k] == ".":
				continue
			if table[j-1][k] == "#" and table[j][k-1] == "#" and table[j-1][k-1] == "#":
				table[j-1][k-1] = "/"
				table[j-1][k] = "\\"
				table[j][k-1] = "\\"
				table[j][k] = "/"

	aa = 0
	for j in xrange(tate):
		if table[j].count("#")>= 1 :
			print "Case #%s:" % (i+1)
			print "Impossible"
			break
		else:		
			aa += table[j].count(".")	
		if j == tate - 1 and aa == tate*yoko:
			print "Case #%s:" % (i+1)
			ans = ["" for _ in xrange(tate)]
			for l in xrange(tate):
				for m in xrange(yoko):
					ans[l] += table[l][m]
				print ans[l]	
		elif j == tate - 1:
			t = 1


	if t == 1:
		print "Case #%s:" % (i+1)
		for j in xrange(tate):
			ans = ""
			for k in xrange(yoko):
				ans += table[j][k]
			print ans
		t = 0
