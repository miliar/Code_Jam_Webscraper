#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


def doit():
	input = open("A.in", 'r')
	output = open("A.out", 'w')
	T = int( input.readline() )
	
	i = 0
	while i < T:
		N = int( input.readline() )
		mat = [ [] for j in range(0,N) ]
		
		j = 0
		while j < N:
			mat[j] = list( input.readline().split('\n')[0] )
			j = j+1
		
		val = compute( N, mat )
		
		output.write( "Case #"+str(i+1)+":\n" )
		for j in val:
			output.write( str(j)+"\n" )
		
		i = i+1
	
	output.close()
	input.close()


def compute( N, mat ):
	RPI = []
	WP = [ 0.0 for i in range(0,N) ]
	WPc = [ 0.0 for i in range(0,N) ]
	OWP = [ 0.0 for i in range(0,N) ]
	OOWP = [ 0.0 for i in range(0,N) ]
	
	i = 0
	while i<N:
		j = 0
		while j<N:
			if mat[i][j] == "1":
				WPc[i] = WPc[i]+1.0
				WP[i] = WP[i]+1.0
			elif mat[i][j] == "0":
				WPc[i] = WPc[i]+1.0
			
			j = j+1
		
		i = i+1
	
	i = 0
	while i<N:
		j = 0
		while j<N:
			if mat[i][j]=="1":
				OWP[i] = OWP[i]+( WP[j]-0.0 )/( WPc[j]-1.0 )
			elif mat[i][j]=="0":
				OWP[i] = OWP[i]+( WP[j]-1.0 )/( WPc[j]-1.0 )
			
			j = j+1
		
		i = i+1
	
	i = 0
	while i<N:
		j = 0
		while j<N:
			if mat[i][j]!=".":
				OOWP[i] = OOWP[i]+OWP[j]/WPc[j]
			
			j = j+1
		
		i = i+1
	
	i = 0
	while i<N:
		WP[i] = WP[i]/WPc[i]
		OWP[i] = OWP[i]/( WPc[i] )
		OOWP[i] = OOWP[i]/( WPc[i] )
		#print i, WP[i], OWP[i], OOWP[i]
		
		RPI.append( WP[i]*0.25 + OWP[i]*0.50 + OOWP[i]*0.25 )
		i = i+1
	
	#print "\n"
	
	return RPI


doit()
