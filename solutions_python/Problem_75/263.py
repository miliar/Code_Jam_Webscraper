#!/usr/bin/python
# -*- coding: utf-8 -*-


def doit():
	input = open("B.in", 'r')
	output = open("B.out", 'w')
	T = int( input.readline() )
	
	i = 0
	while i < T:
		line = input.readline().split()
		
		comb = {}
		neg = {}
		spell = []
		
		C = int( line.pop(0) )
		while C > 0:
			tmp = line.pop(0)
			comb[ tmp[0] ] = ( tmp[1], tmp[2] )
			comb[ tmp[1] ] = ( tmp[0], tmp[2] )
			
			C = C-1
		
		
		D = int( line.pop(0) )
		while D > 0:
			tmp = line.pop(0)
			neg[ tmp[0] ] = tmp[1]
			neg[ tmp[1] ] = tmp[0]
			
			D = D-1
		
		N = int( line.pop(0) )
		spell = list( line.pop(0) )
		
		#print neg, comb
		out = compute( comb, neg, spell )
		
		output.write( "Case #"+str(i+1)+": "+out+"\n" )
		
		i = i+1
	
	output.close()
	input.close()


def compute(  comb, neg, spell ):
	out = []
	out_s = '['
	pending = {}
	
	N = len( spell )
	
	while N > 0:
		N = N-1
		
		c = spell.pop(0)
		#print out, c, pending
		
		if len(out) > 0 and c in comb:
			if comb[c][0] == out[ len(out)-1 ]:
				t = out[ len(out)-1 ]
				
				if t in neg and neg[t] in pending and pending[ neg[t] ] == len(out)-1:
					pending.pop( neg[t] )
				
				out.pop()
				out.append( comb[c][1] )
				
				continue
		
		if c in pending:
			while len(out) > pending[c]:
				out = []
			
			pending = {}
			
			continue
		
		if c in neg:
			if not neg[c] in pending:
				pending[ neg[c] ] = len(out)
		
		out.append( c )
	
	#print out, '\n'
	
	i = 0
	while i < len(out):
		out_s = out_s+out[i]
		
		if i+1 < len(out):
			out_s = out_s+", "
		
		i = i+1
	
	return out_s+']'


doit()
