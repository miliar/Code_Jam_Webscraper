import math
import heapq

archivo=open('C-small-2-attempt1.in')
archivo.readline()

lista=[]


for linea in archivo.readlines():
	lista.append(linea.split())
	
def log2( x ):
	return int(math.log( x ) / math.log( 2 ))
 
def funcion1(n):
	if n==0:
		return (0,0)
	if n%2==0:
		return ((n/2)-1, n/2)
	else:
		return (n/2, n/2)
		
	
def funcion2(N, K):
	array=[0]*(2**(log2(K)+1))
	array[1]=funcion1(N)
	
	for i in xrange (1, 2**(log2(K))):
		array[i*2]=funcion1(array[i][0])
		array[i*2+1]=funcion1(array[i][1])
	listita=sorted(array[2**(log2(K)):2**(log2(K)+1)+1])
	return max(listita [(K-2**(log2(K)))*(-1)-1]), min(listita [(K-2**(log2(K)))*(-1)-1])
	
	


for numCase, case in enumerate(lista):
	print "Case #{}: {}".format(numCase+1, funcion2 (int(case[0]), int(case[1])))

	

		

