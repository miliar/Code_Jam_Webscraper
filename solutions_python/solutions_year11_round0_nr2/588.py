#!/usr/bin/python

from sys import stdin




def combine_compare( a, b ):
	b1=b[0]+b[1]
	b2=b[1]+b[0]
	return (a==b1 or a==b2)

def combine( com, a ):
	isCombined = False
	for b in com:
		if combine_compare( a, b ) :
			isCombined = b[2]
			break
	return isCombined

def oppose_compare( a, b ):
	return combine_compare( a, b )

def oppose( opp, string):
	isOppose = False
	l = len(string)
	last = string[l-1:]
	for c in opp:
		i=0
		while(i<l-1):
			a=string[i:i+1]+last
			if oppose_compare( a, c ):
				isOppose = True
				break
			i=i+1
		if isOppose:
			break
	return isOppose



T=int(stdin.readline())
j=0
while(j<T):
	inp = stdin.readline().split() #read each line

	Combine_=[]
	Oppose_=[]

	#store Combine pairs
	C=int(inp.pop(0))
	k=0
	while(k<C):
		Combine_.append( inp.pop(0) )
		k=k+1
	#store Oppose pairs	
	D=int(inp.pop(0))
	k=0
	while(k<D):
		Oppose_.append( inp.pop(0) )
		k+=1
	
	
	
	N=int( inp.pop(0) )	
	test=inp.pop(0)

	result = ""
	length=0  #length of result
	last = ""
	i=0
	while(i<N):
		invoke = test[i]
		isCombined=combine( Combine_, result[length-1:]+invoke )
		if( isCombined ):
			result = result[0:length-1] + isCombined
		else:
			result = result + invoke
			length = length+1
			if oppose( Oppose_, result ):
				result = ""
				length=0
		i=i+1 #invoke next basement

	print "Case #"+str(j+1)+": ["+", ".join( list( result ) ) + "]"
	j=j+1 #read next line
				

