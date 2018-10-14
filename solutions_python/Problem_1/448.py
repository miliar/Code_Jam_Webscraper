#! /usr/bin/env python
# -*- coding: utf8 -*-

N = int(raw_input())
X = 0
Y = 0

while X < N:
	S = int(raw_input())
	engine = []
	while S > 0:
		engine.append(raw_input())
		S = S - 1
		
	Q = int(raw_input())
	query = []
	while Q > 0:
		query.append(raw_input())
		Q = Q - 1
		
	engine_bak = engine[:] # engine backup
	for q in query:
		if engine.count(q) != 0:
			if len(engine) > 1:
				engine.remove(q)
			else:
				Y = Y + 1
				engine = engine_bak[:]
				if engine.count(q) != 0:
					if len(engine) > 1:
						engine.remove(q)
		
	print "Case #" + str(X+1) + ": " + str(Y)
	
	X = X + 1
	Y = 0