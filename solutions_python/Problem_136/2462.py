#!/usr/bin/python

T = int(raw_input())

def timeNeeded(currentProduction, c, f, x, timeSoFar):
	if x/currentProduction < c/currentProduction + x/(currentProduction + f):
		return timeSoFar + x/currentProduction
	return timeNeeded(currentProduction + f, c, f, x, timeSoFar + c/currentProduction)
	

for t in xrange(T):
	C, F, X = map(float, raw_input().split())
	currentProduction = 2
	timeSoFar = 0
	while X/currentProduction > C/currentProduction + X/(currentProduction + F):
		timeSoFar += C/currentProduction
		currentProduction += F
	timeSoFar += X/(currentProduction)
	
	print "Case #%d: %.7f" % (t+1, timeSoFar)