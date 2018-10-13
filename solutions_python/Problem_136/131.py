#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# google code jam - c.durr- 2014

# CookieClickerAlpha
# https://code.google.com/codejam/contest/2974486/dashboard#s=p1
# 
# 

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

for test in range(readint()):
	c,f,x = readarray(float)
	t = 0 # time until last farm purchase
	k = 0 # number of farms purchased so far
	# there are at most 10^5 iterations
	while t+x/(2+k*f) > t+c/(2+k*f)+x/(2+k*f+f):
		t += c/(2+k*f)
		k += 1
	print "Case #%i:"% (test+1), t+x/(2+k*f)
