#!/usr/bin/python
import sys
import string
import pdb
archivo=sys.argv[1]
fd=open(archivo)
Ncases=int(fd.readline())
for j in range(Ncases):
	Nuniv=int(fd.readline())
	universos=[]
	for u in range(Nuniv):
		universos.append(fd.readline())
	Nqueries=int(fd.readline())
	queries=[]
	for q in range(Nqueries):
		queries.append(fd.readline())
	#
	#print universos	
	#print queries
	combo=list(universos)
	cambios=0
#	pdb.set_trace()
	for qy in queries:	
		for uv in combo:
			if uv==qy:
				if len(combo)>1:
					combo.remove(uv)
					break
				else:
					combo=list(universos)
					combo.remove(uv)
					cambios+=1
					break

#	print cambios
	print("Case #"+str(j+1)+": "+str(cambios))




	
		
	
#	print("Case #"+str(j+1)+": "+msg)
