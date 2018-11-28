#! /urs/bin/python

from numpy import *
from decimal import *

f_in = open ('B-large.in','r')

f_out = open ('B-large.out','w')

def checklista ( lista, op, co):
	for z in co:
#		print lista
		if ((lista[len(lista)-1]==z[0] and lista[len(lista)-2]==z[1]) or (lista[len(lista)-1]==z[1] and lista[len(lista)-2]==z[0])) and (len(lista)>1):
			lista=lista[0:len(lista)-2]
#			print '->'
#			print lista
			lista.append(z[2])
#			print lista
	for k in op:
		for j in range(len(lista)-1):
			if (lista[len(lista)-1]==k[0] and lista[j]==k[1]) or (lista[len(lista)-1]==k[1] and lista[j]==k[0]):
				lista=[]	
				return lista
	return lista
NN = int(f_in.readline())
v=[]
for case in range(NN):
	co=[]
	h=[]
	op=[]	
	v=f_in.readline().split()
	C=int(v[0])
	for u in range(C):
		co.append(v[1+u])
	D=int(v[C+1])
	for o in range(D):
		op.append(v[C+2+o])
	N=int(v[C+D+2])
	lista=[]
#	print case
#	print co
#	print op
#	print C
#	print D
#	print N
	for g in range(N):
		lista.append(v[C+D+3][g])
		lista=checklista(lista,op,co)
	f_out.write ('Case #' + str(case+1) + ': [')
	for l in range(len(lista)):
		f_out.write (lista[l])
		if l==len(lista)-1:
			f_out.write ('')			
		else:
			f_out.write (', ')			
	f_out.write (']\n')
	print lista
f_out.close()
